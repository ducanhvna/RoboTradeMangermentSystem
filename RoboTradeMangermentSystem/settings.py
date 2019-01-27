"""
Django settings for RoboTradeMangermentSystem project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^vhitx*e$9h6ye7@2wx2)h(-acs1crfs=$-wbkbmxc4g8i&o@)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RoboTradeMangermentSystem.urls'

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

WSGI_APPLICATION = 'RoboTradeMangermentSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# AUTH_USER_MODEL = 'common.User'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ROOT = BASE_DIR + '/static/'
COMPRESS_URL = STATIC_URL
COMPRESS_ENABLED = True

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_REBUILD_TIMEOUT = 5400


COMPRESS_OUTPUT_DIR = 'CACHE'
COMPRESS_URL = STATIC_URL
COMPRESS_ENABLED = True

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': 'STATIC_URL',
}
DEFAULT_FROM_EMAIL = 'no-reply@django-crm.micropyramid.com'
MAIL_SENDER = 'AMAZON'
INACTIVE_MAIL_SENDER = 'MANDRILL'

AM_ACCESS_KEY = os.getenv('AM_ACCESS_KEY', '')
AM_PASS_KEY = os.getenv('AM_PASS_KEY', '')
AWS_REGION = os.getenv('AWS_REGION', '')

MGUN_API_URL = os.getenv('MGUN_API_URL', '')
MGUN_API_KEY = os.getenv('MGUN_API_KEY', '')

SG_USER = os.getenv('SG_USER', '')
SG_PWD = os.getenv('SG_PWD', '')

MANDRILL_API_KEY = os.getenv('MANDRILL_API_KEY', '')

ADMIN_EMAIL = "ducanhvna@outlook.com"

try:
    from .dev_settings import *
except ImportError:
    pass
