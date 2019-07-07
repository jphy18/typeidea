# -*- coding: utf-8 -*-
"""
@Author  : jphy181202@gmail.com
@Time    : 2019/7/7 11:33
"""
from .base import * # NOQA

DEBUG = True
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}