from catalogues.settings.common import *
import logging
import dj_database_url


DEBUG = os.environ.get('DEBUG_PROD')

# SESSION_COOKIE_SECURE=True
# SECURE_SSL_REDIRECT=True
# CSRF_COOKIE_SECURE=True

SECRET_KEY = os.environ.get('SECRET_KEY_PROD')

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

print("======================os.getenv('DB_USER_PROD') :", os.getenv('DB_USER_PROD'))
print("======================os.environ.get('DB_NAME_PROD'):", os.environ.get('DB_NAME_PROD'))

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME_PROD'),
        'USER': os.environ.get('DB_USER_PROD'),
        'PASSWORD': os.environ.get('DB_PASSWORD_PROD'),
        'HOST': os.environ.get('HOST_PROD'),
        'PORT': os.environ.get('PORT_PROD'),
    }
}
