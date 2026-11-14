#!/usr/bin/env python3
"""Read-only web service for the Harold AI Pool extension registry.

Run with ``gunicorn app:app`` (Render default) or ``python app.py``.
Binds to the PORT environment variable (default 10000).
"""

import json
import os

from manage_extensions import load

ROUTES = ("/", "/health", "/extensions")


def _json(start_response, status, payload):
    body = json.dumps(payload).encode("utf-8")
    start_response(status, [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(body))),
    ])
    return [body]


def app(environ, start_response):
    path = environ.get("PATH_INFO", "/").rstrip("/") or "/"
    if environ.get("REQUEST_METHOD", "GET") not in ("GET", "HEAD"):
        return _json(start_response, "405 Method Not Allowed", {"error": "read-only service"})
    if path == "/health":
        return _json(start_response, "200 OK", {"status": "ok"})
    if path == "/extensions":
        try:
            return _json(start_response, "200 OK", load())
        except (OSError, ValueError):
            return _json(start_response, "500 Internal Server Error", {"error": "registry unavailable"})
    if path == "/":
        return _json(start_response, "200 OK", {"service": "harold-ai-pool", "routes": list(ROUTES)})
    return _json(start_response, "404 Not Found", {"error": "not found"})


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    port = int(os.environ.get("PORT", "10000"))
    with make_server("0.0.0.0", port, app) as server:
        print(f"Harold AI Pool listening on port {port}")
        server.serve_forever()
