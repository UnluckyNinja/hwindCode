# -*- coding: utf-8 -*-
from .base import *
DEBUG = True

SITE_ID = 3

DATABASES = GetConfig("Databases")

ALLOWED_HOSTS = ['*']