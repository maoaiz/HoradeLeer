# encoding:utf-8
"""
Django settings for HoradeLeer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_NAME = "Hora de Leer"

ADMINS = (
    ('Mauricio Aizaga', 'mauricioaizaga@gmail.com'),
)

APPS = tuple()
folder_apps = ["apps"]

for app in folder_apps:
    APPS += tuple([app+"."+x for x in os.listdir(os.sep.join([BASE_DIR,app])) if os.path.isdir(os.sep.join([BASE_DIR,app,x]))])


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h5it^$6^k_-d*ndx$ve-25f3@&=f^!$ufp#3yo=hbp7nbx-7o#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
) + APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'HoradeLeer.urls'

WSGI_APPLICATION = 'HoradeLeer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

try:
    from .local_settings import DATABASES
except ImportError:
    DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': os.path.join(BASE_DIR, 'db.sqlite3'),'USER': '','PASSWORD': '','HOST': '','PORT': '',}}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR , 'public/static').replace('\\','/'),
)


LOCALE_PATHS = tuple([os.sep.join([BASE_DIR,APP.replace('.',os.sep),'locale']) for APP in APPS])
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = "/"
