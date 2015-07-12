# -*- coding: utf-8 -*-
from .base import *
DEBUG = False

DATABASES = GetConfig("Databases")

STATIC_ROOT = '/var/www/pyvideo_project/staticfiles'

ALLOWED_HOSTS = ['*']