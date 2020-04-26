from dotenv import load_dotenv

"""
Django settings for chatroom_app project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'te=lepr$6guag+*i9#w2vy0yk(3@6%q%ky+=7v7!m-9yx^!&iy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django_extensions',
    'chat.apps.ChatConfig',
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

ROOT_URLCONF = 'chatroom_app.urls'

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

WSGI_APPLICATION = 'chatroom_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# TWILIO_ACCOUNT_SID = os.environ.get('AC36ed39d83df601dd61b49495cb5f6d3f', None)
# TWILIO_API_KEY = os.environ.get('SK92144a7e40fca11f434a4a6c01589e01', None)
# TWILIO_API_SECRET = os.environ.get('IMnZmbql2oe5Cs5Bj9wqb0hmno7XLAkI', None)
# TWILIO_CHAT_SERVICE_SID = os.environ.get('ISae647ca731f148c3a39381602a87865c', None)


# TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID','ACc84c3591272f4c8c109b6368c8312b77')
# TWILIO_API_KEY = os.environ.get('TWILIO_API_KEY','SK627a1009d1c8a4522d8ba58dc7598f09')
# TWILIO_API_SECRET = os.environ.get('TWILIO_API_SECRET','wykN89LFMkSLpfwuPbzSR9h8fxA8AYYH')
# TWILIO_CHAT_SERVICE_SID = os.environ.get('TWILIO_CHAT_SERVICE_SID','IS7f4f9d1fd215416aa08e5baad0500d81')

# TWILIO_ACCOUNT_SID = os.environ.get('ACc84c3591272f4c8c109b6368c8312b77',None)
# TWILIO_API_KEY = os.environ.get('SK627a1009d1c8a4522d8ba58dc7598f09',None)
# TWILIO_API_SECRET = os.environ.get('wykN89LFMkSLpfwuPbzSR9h8fxA8AYYH',None)
# TWILIO_CHAT_SERVICE_SID = os.environ.get('IS7f4f9d1fd215416aa08e5baad0500d81',None)

# Twilio config
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_API_KEY = os.environ.get('TWILIO_API_KEY', None)
TWILIO_API_SECRET = os.environ.get('TWILIO_API_SECRET', None)
TWILIO_CHAT_SERVICE_SID = os.environ.get('TWILIO_CHAT_SERVICE_SID', None)