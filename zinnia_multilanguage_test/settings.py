# -*- coding: utf-8 -*-
"""
Luiz C. Mostaço-Guidolin

Add multi-language post support to Zinnia and Django.

Based on the documentation from
http://codeispoetry.me/index.php/django-blog-zinnia-multilanguage-support-with-django-modeltranslation/
"""

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
MODELTRANSLATION_DEBUG = True

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ( 'en', _('English') ),
    ( 'pt-br', _('Portuguese') ),
]

#MODELTRANSLATION SETTINGS
MODELTRANSLATION_TRANSLATION_FILES = (
    'zinnia_multilanguage_test.translation',
)
MODELTRANSLATION_AUTO_POPULATE = True
MODELTRANSLATION_FALLBACK_LANGUAGES = (
    'en',
    'pt-br',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Your_secret_key_here'

ALLOWED_HOSTS = []

ROOT_URLCONF = 'demo_zinnia_wymeditor.urls'

INSTALLED_APPS = (
    # it is very important to have modeltranslation as one of the
    # first modules to be loaded !!
    'modeltranslation',
    'debug_toolbar',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.admin',
    'django_comments',
    # third party apps (zinnia reqs.)
    'mptt',
    'tagging',
    'zinnia',
    'zinnia_wymeditor',
    # my apps
    'zinnia_multilanguage_test',
)

# Added because of zinnia
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'zinnia.context_processors.version',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Added for i18n, must come after Session and before Common, if Cache is
    # used must come after it
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zinnia_multilanguage_test.urls'
WSGI_APPLICATION = 'zinnia_multilanguage_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
