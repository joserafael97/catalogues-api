from catalogues.settings.common import *


SECRET_KEY = env('SECRET_KEY_DEV')

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG_DEV')

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME_DEV'),
        'USER': env('DB_USER_DEV'),
        'PASSWORD': env('DB_PASSWORD_DEV'),
        'HOST': env('HOST_DEV'),
        'PORT': env('PORT_DEV'),
    }
}
