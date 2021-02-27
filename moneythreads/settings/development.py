from project_name.settings.production import *

DB_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, 'db'))

DEBUG = TEMPLATE_DEBUG = True
SECRET = '42'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_PATH, 'db.sqlite3'),
    }
}

INTERNAL_IPS = ('127.0.0.1',)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
