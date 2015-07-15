# -*- coding: utf-8 -*-
"""
WSGI config for pyvideo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append("/var/www/pyvideo_project")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyvideo.settings.production")

application = get_wsgi_application()
