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
	"""Settings for local sqlite database. If you don't already have a database,
	   one will be created for you. Don't keep the database in source control."""
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(SITE_ROOT, '***YOUR_DATABASE_NAME***.db')),
    }
}

ADMIN_USERNAME = '***YOUR_ADMIN_USERNAME***'
ADMIN_PASSWORD = '***YOUR_ADMIN_PASSWORD***'



INTERNAL_IPS = ("127.0.0.1",)

EMAIL_HOST = "localhost"
EMAIL_POST = 1025

