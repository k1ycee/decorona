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

ADMINS = (
("Nolwac", "connect2globalvill@gmail.com"),
)
# Application definition

INSTALLED_APPS = [
     #here are my own apps
    'accounts',
    #this one is django specific apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #here are third party apps
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'rest_auth',
    'django.contrib.sites',
    'rest_auth.registration',
    'django_filters',
    'corsheaders',
    'AutoTags',
    'django_channels_chat',
    'channels',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
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

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend"
)
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

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

CORS_ORIGIN_WHITELIST = (
 'localhost:8080',
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'decorona_static', 'static')#make sure to change the static root later to hagent static root

# This very one is for the media files and how to get hold of them.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'decorona_media', 'media')#make sure to change the media root later to hagent media root.

ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION ="mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = '/account/login'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 4
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'DeCorona'
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_BLACKLIST = ['DeCorona', 'Nolwac', 'DeCovid', 'Decorona', 'decorona']
OLD_PASSWORD_FIELD_ENABLED = True
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