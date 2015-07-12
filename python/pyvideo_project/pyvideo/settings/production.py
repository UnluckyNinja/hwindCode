# -*- coding: utf-8 -*-
from .base import *
DEBUG = True

DATABASES = GetConfig("Databases")

STATIC_ROOT = '/var/www/pyvideo_project/pyvideo/static'