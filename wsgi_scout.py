"""Smart WSGI entry for Render: auto-detects Django settings module.
Place this file at repo root. Start Command:
  gunicorn wsgi_scout:application --preload --timeout 120
Order:
1) Use DJANGO_SETTINGS_MODULE if set
2) Scan repo for */settings.py with __init__.py and pick the shallowest
"""
import os
from pathlib import Path

def _detect_settings_module(search_root: Path):
    candidates = []
    for p in search_root.rglob('settings.py'):
        s = str(p)
        if any(skip in s for skip in ('/.venv/', '/venv/', '/site-packages/', '/node_modules/')):
            continue
        pkg = p.parent
        if not (pkg / '__init__.py').exists():
            continue
        try:
            rel = p.parent.relative_to(search_root)
        except ValueError:
            continue
        mod = '.'.join(rel.parts + ('settings',))
        candidates.append((len(rel.parts), mod))
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0])
    return candidates[0][1]

mod = os.environ.get('DJANGO_SETTINGS_MODULE')
if not mod:
    repo_root = Path(__file__).resolve().parent
    mod = _detect_settings_module(repo_root)

if not mod:
    raise RuntimeError('Could not detect DJANGO_SETTINGS_MODULE.')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', mod)

from django.core.wsgi import get_wsgi_application  # noqa: E402
application = get_wsgi_application()
