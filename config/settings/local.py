from .base import *  # noqa
from .base import env

# GENERAL
DEBUG = True
SECRET_KEY = 'django-insecure-local-dev-key'
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

# CACHES
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    }
}

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-debug-toolbar
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': ['debug_toolbar.panels.redirects.RedirectsPanel'],
    'SHOW_TEMPLATE_CONTEXT': True,
}
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # noqa F405
    }
} 