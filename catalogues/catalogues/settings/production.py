from catalogues.settings.common import *

DEBUG = env('DEBUG_PROD')

SECRET_KEY = env('SECRET_KEY_PROD')

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME_PROD'),
        'USER': env('DB_USER_PROD'),
        'PASSWORD': env('DB_PASSWORD_PROD'),
        'HOST': env('HOST_PROD'),
        'PORT': env('PORT_PROD'),
    }
}