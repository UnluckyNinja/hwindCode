# -*- coding: utf-8 -*-
from .base import *
DEBUG = False

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

SITE_ID = 4

DATABASES = GetConfig("Databases")

ALLOWED_HOSTS = ['*']