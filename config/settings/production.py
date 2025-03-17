from .base import *  # noqa
from .base import env

# GENERAL
DEBUG = False
SECRET_KEY = env('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

# DATABASES
DATABASES['default'] = env.db('DATABASE_URL')  # noqa F405
DATABASES['default']['ATOMIC_REQUESTS'] = True  # noqa F405
DATABASES['default']['CONN_MAX_AGE'] = env.int('CONN_MAX_AGE', default=60)  # noqa F405

# SECURITY
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# STATIC
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# TEMPLATES
TEMPLATES[0]['OPTIONS']['loaders'] = [  # noqa F405
    (
        'django.template.loaders.cached.Loader',
        [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]
    ),
]

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('DJANGO_EMAIL_HOST')
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# ADMIN
ADMIN_URL = env('DJANGO_ADMIN_URL', default='admin/') 