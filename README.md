# Harold AI Pool

Read-only web service for the pool's VS Code extension registry.

- `GET /health` returns `{"status": "ok"}`
- `GET /extensions` returns `extensions/registry.json`

Run locally with `python app.py` (uses the `PORT` variable, default 10000) or `gunicorn app:app`.
On Render: build `pip install -r requirements.txt`, start `gunicorn app:app` (see `render.yaml`).
Manage the registry with `manage_extensions.py` (see `extensions/README.md`).
