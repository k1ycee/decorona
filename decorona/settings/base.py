"""
Django settings for EduTech project.

Generated by 'django-admin startproject' using Django 1.11.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django_channels_chat.settings import * #this is to include the channels Chat setting for the project itself.
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6x==q#)twsxmnc9bw0g!^9obkx!&#qh+ep@f1uc0ejyg)^pen%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'snappynolwac@gmail.com'
EMAIL_HOST_PASSWORD = 'nolwac15-04-1996mydjangoweb'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = [
    #this one is django specific apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #here are my own apps
    'accounts',
    #here are third party apps
    'rest_framework',
    'AutoTags',
    'django_channels_chat',
    'channels',
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

ROOT_URLCONF = os.path.split(BASE_DIR)[1]+'.urls' #See the os module and also see the variable BASE_DIR.

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

WSGI_APPLICATION = os.path.split(BASE_DIR)[1]+'.wsgi.application'
ASGI_APPLICATION = os.path.split(BASE_DIR)[1]+'.routing.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CHANNEL_LAYERS={
    'default':{
            'BACKEND':'channels_redis.core.RedisChannelLayer',
            'CONFIG':{
            'hosts':[('localhost', 6379)],
            },
    },
}
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# djang-heroku setting
import django_heroku
django_heroku.settings(locals())

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'decorona_static', 'static')#make sure to change the static root later to hagent static root

# This very one is for the media files and how to get hold of them.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'decorona_media', 'media')#make sure to change the media root later to hagent media root.

#There have beeen a little issue with django version so in other to avoid such problems I have decided to find a way of knowing the particular
#django version that I am dealing with and to also do somethings with respect to them.
#so the piece of code below is to know the django version and to be able to do comparism with them in my code.

from django import __version__ as djv
ver = list(djv)
ver[3:] = ''
DJANGO_VERSION = float(''.join(ver))
#the above 3 lines of code gets us the django version we are dealing with in the project as a float.



#THE BELOW SETTINGS ARE FOR AUTOTAGS APP
LOGIN_INCLUSION_TEMPLATE='accounts/login_template.html'