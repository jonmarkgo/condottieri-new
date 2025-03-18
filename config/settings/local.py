from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-development-key-change-this-in-production'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Development hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'local.jonmarkgo.com']

# Development security settings - override production settings for local dev
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_DOMAIN = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_DOMAIN = None
SECURE_SSL_REDIRECT = False

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'condottieri',
        'USER': 'postgres',
        'PASSWORD': 'abc123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debug toolbar configuration
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
    'RESULTS_CACHE_SIZE': 100,
}

# Debug toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
INTERNAL_IPS = ['127.0.0.1']

# Scenarios
SCENARIOS_ROOT = 'scenarios' 