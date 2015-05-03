# settings/template.local.py

"""
# Local Settings Template

  * Copy this file into a local.py file, then fill in the details of this file for 
    the specifics of your project. Each developer should make their own local settings
    file and it should not be kept in source control as it will contain secret 
    information such as admin passwords and api keys. 

  * Values you need to replace are surounded by triple *'s:

      e.g. ***REPLACE_THIS***

"""
from os.path import join, normpath
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(SITE_ROOT, 'tour.db')),
    }
}

ADMIN_USERNAME = 'demo'
ADMIN_PASSWORD = 'demo'

ROOT_DOMAIN = 'localhost:8000'


INTERNAL_IPS = ("127.0.0.1",)

EMAIL_HOST = "localhost"
EMAIL_POST = 1025

