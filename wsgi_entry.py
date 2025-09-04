"""Generic WSGI entry for Gunicorn on Render."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ.get('DJANGO_SETTINGS_MODULE', 'backend.settings'))
application = get_wsgi_application()
