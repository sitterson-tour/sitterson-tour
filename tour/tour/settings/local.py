# settings/local.py
from os.path import join, normpath
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

databases = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(DJANGO_ROOT, 'tournamint.db')),
    }
}

INTERNAL_IPS = ("127.0.0.1",)

EMAIL_HOST = "localhost"
EMAIL_POST = 1025

