# -*- coding: utf-8 -*-
from .base import *
DEBUG = False

DATABASES = GetConfig("Databases")

ALLOWED_HOSTS = ['*']