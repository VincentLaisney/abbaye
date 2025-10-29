"""
WSGI config for abbaye project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os,sys

sys.path.append('/home/vincent/.local/lib/python3.12/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abbaye.settings')

application = get_wsgi_application()
