# settings/production.py

from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['tournamint.cs.unc.edu']


DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tournamint_db',
		'USER': 'tournamint',
		'PASSWORD': 'tournamint',
		'HOST': 'localhost',
		'PORT': '5432',
    }
}
