"""
Django settings for pytx project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', None)

ALLOWED_HOSTS = [
    'localhost',
    'cool-sea-0598.graviton.ninja',
    'pytexas.herokuapp.com',
    'www.pytexas.org',
    'pytexas.org',
    '.pytexas.org',
]

# Application definition

INSTALLED_APPS = [
    'flat_responsive',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djzen',
    'django_filters',
    'conference.profiles',
    'conference.event',
    'graphene_django',
    'raven.contrib.django.raven_compat',
    'rest_framework',
    'pytx',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pytx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pytx.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# AUTH_USER_MODEL = 'profiles.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

FRONTEND = '2019-dist'
FRONTEND_DIR = os.environ.get('FRONTEND_DIR',
                              os.path.join(BASE_DIR, 'node_modules', 'pytexas2019'))
FRONTEND_TEMPLATES = os.path.join(os.path.dirname(FRONTEND_DIR), 'src')
FRONTEND_MD = os.path.join(FRONTEND_DIR, 'md')

STATIC_URL = '/static-2019/'

STATIC_ROOT = os.path.join(BASE_DIR, "static-compiled")

# Uncomment for forever-cacheable files and compression support
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dist'),
    os.path.join(BASE_DIR, 'node_modules/vuetify/dist'),
]

# Uncomment if using Heroku
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "sessions"

MEMCACHE = {
    'BACKEND': 'django_bmemcached.memcached.BMemcached',
    'LOCATION': os.environ.get('MEMCACHEDCLOUD_SERVERS', '').split(','),
    'OPTIONS': {
        'username': os.environ.get('MEMCACHEDCLOUD_USERNAME', ''),
        'password': os.environ.get('MEMCACHEDCLOUD_PASSWORD', '')
    }
}

CACHES = {
    'default': MEMCACHE,
    'sessions': MEMCACHE,
}

AUTH_USER_MODEL = 'profiles.User'

GRAPHENE = {'SCHEMA': 'pytx.schema.schema'}

CURRENT_CONF = '2019'

STRIPE_PUB_KEY = os.environ.get('STRIPE_PUB_KEY', '')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')

SERVER_EMAIL = 'conference@pytexas.org'
DEFAULT_FROM_EMAIL = 'conference@pytexas.org'

EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('AWS_ACCESS_KEY', '')
EMAIL_HOST_PASSWORD = os.environ.get('AWS_SECRET_KEY', '')
EMAIL_USE_TLS = True

EVENTBRITE_API_URL = 'https://www.eventbriteapi.com/v3'
EVENTBRITE_EVENT_ID = os.environ.get('EVENTBRITE_EVENT_ID', '')
EVENTBRITE_OAUTH_TOKEN = os.environ.get('EVENTBRITE_OAUTH_TOKEN', '')

from pytx.settings.logging import *
