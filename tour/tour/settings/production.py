# settings/production.py

from os.path import join, normpath
from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['tournamint.cs.unc.edu']


DATABASES = {
  'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(SITE_ROOT, 'tour.db')),
    }
}
