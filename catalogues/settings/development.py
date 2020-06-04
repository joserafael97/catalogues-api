from catalogues.settings.common import *

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:4200',
]

CORS_ORIGIN_REGEX_WHITELIST = [
    'http://localhost:4200',
]

SECRET_KEY = os.getenv('SECRET_KEY_DEV')

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['*']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG_DEV')

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME_DEV'),
        'USER': os.getenv('DB_USER_DEV'),
        'PASSWORD': os.getenv('DB_PASSWORD_DEV'),
        'HOST': os.getenv('HOST_DEV'),
        'PORT': os.getenv('PORT_DEV'),
    }
}
