#!/usr/bin/env python3
"""Simple extension manager for the Harold AI Pool."""

import json
import sys
from pathlib import Path

REGISTRY = Path(__file__).parent / "extensions" / "registry.json"


def load():
    if not REGISTRY.exists():
        return {"extensions": []}
    with open(REGISTRY) as f:
        return json.load(f)


def save(data):
    REGISTRY.parent.mkdir(exist_ok=True)
    with open(REGISTRY, "w") as f:
        json.dump(data, f, indent=2)


def add(name, publisher, description):
    data = load()
    if any(e["name"] == name for e in data["extensions"]):
        print(f"Extension '{name}' already exists.")
        return
    data["extensions"].append({
        "name": name,
        "type": "vscode-extension",
        "description": description,
        "publisher": publisher,
        "setup": f"code --install-extension {publisher}.{name}"
    })
    save(data)
    print(f"Added '{name}'.")


def list_exts():
    data = load()
    if not data["extensions"]:
        print("No extensions registered.")
        return
    for e in data["extensions"]:
        print(f"  {e['name']} - {e['description']} (by {e['publisher']})")


def remove(name):
    data = load()
    data["extensions"] = [e for e in data["extensions"] if e["name"] != name]
    save(data)
    print(f"Removed '{name}'.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "add":
        add(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "")
    elif cmd == "list":
        list_exts()
    elif cmd == "remove":
        remove(sys.argv[2])
    else:
        print("Usage: manage_extensions.py add|list|remove ...")