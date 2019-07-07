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
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'typeidea',  # 你要存储数据的库名，事先要创建之
        'USER': 'ywh',  # 数据库用户名
        'PASSWORD': 'ywh123456',  # 密码
        'HOST': 'localhost',  # 主机
        'PORT': '3306',  # 数据库使用的端口
    }
}