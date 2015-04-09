from os.path import abspath, basename, dirname, join, normpath
from sys import path



DJANGO_ROOT = dirname(dirname(abspath(__file__)))

SITE_ROOT = dirname(DJANGO_ROOT)

SITE_NAME = basename(DJANGO_ROOT)

path.append(DJANGO_ROOT)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sq!7+g1&uq#fn#!+1h5%kti%l1y!-s+d3_lsk%z0hn-pi-85#8'

# SECURITY WARNING: don't run with debug turned on in production!


ADMINS = (
	('Curtis Bowman', 'c.bowman1711@gmail.com'),
)

MANAGERS = ADMINS

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'grappelli',
    'bootstrap3',
	'south',
)

LOCAL_APPS = (
'tour',
)

INSTALLED_APPS = THIRD_PARTY_APPS + LOCAL_APPS + DJANGO_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application' 

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

MEDIA_URL = '/media/'

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
	normpath(join(SITE_ROOT, 'assets')),
)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = (
	normpath(join(SITE_ROOT, 'templates')),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

