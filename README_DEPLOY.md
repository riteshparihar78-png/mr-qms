# QMS Portal — Render Ready Package

Detected project module: **backend** (from `manage.py` / `settings.py`).

## Build & Start
- Build: `pip install -r requirements.txt`
- Start: `gunicorn wsgi_entry:application --preload --timeout 120`

## Environment
- DJANGO_SETTINGS_MODULE=backend.settings
- DATABASE_URL is auto-wired by render.yaml when using Blueprint.

## Post-deploy
- Migrations & collectstatic run automatically via Blueprint.
