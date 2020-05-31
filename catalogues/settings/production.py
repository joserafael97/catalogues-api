from catalogues.settings.common import *

DEBUG = env('DEBUG_PROD')

# SESSION_COOKIE_SECURE=True
# SECURE_SSL_REDIRECT=True
# CSRF_COOKIE_SECURE=True

SECRET_KEY = env('SECRET_KEY_PROD')

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}