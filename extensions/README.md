# Harold AI Pool Extensions

Plug your VS Code extensions into the chat pool here.

## Quick Add

Edit `extensions/registry.json` and add your extension:

```json
{
  "extensions": [
    {
      "name": "my-extension",
      "type": "vscode-extension",
      "description": "What my extension does",
      "publisher": "your-name",
      "setup": "code --install-extension your-name.my-extension"
    }
  ]
}
```

## Or use the manager:

```bash
python3 manage_extensions.py add my-extension "Your Name" "Description"
python3 manage_extensions.py list
python3 manage_extensions.py remove my-extension
```