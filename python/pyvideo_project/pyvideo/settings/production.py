# -*- coding: utf-8 -*-
from .base import *
DEBUG = True

DATABASES = GetConfig("Databases")

ALLOWED_HOSTS = ['*']