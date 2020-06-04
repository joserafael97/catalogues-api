from catalogues.settings.common import *


SECRET_KEY = os.getenv('SECRET_KEY_DEV')

DEBUG = os.getenv('DEBUG_DEV')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'catalogues-tester.db'),
    }
}
