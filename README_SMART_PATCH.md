# Render Smart Patch (Drop-in)

Copy these files to your repo **root** and commit. They fix:
- Hard-coded `backend` WSGI import (auto-detects your settings module)
- Wrong Python (pins 3.12.5)
- Missing build/start commands and envs

## Files
- wsgi_scout.py
- Procfile
- render.yaml
- runtime.txt
- requirements.txt (template; keep your own if you already have one)
- .env.sample

## Render
- Build: `pip install -r requirements.txt`
- Start: `gunicorn wsgi_scout:application --preload --timeout 120`

Use `render.yaml` (Blueprint) for auto database + migrations.
