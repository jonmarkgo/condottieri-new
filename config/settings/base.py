"""
Base settings for Condottieri project.
"""
import os
from pathlib import Path
import environ

# Compatibility patches for older Django code
from django.utils import encoding
def python_2_unicode_compatible(klass):
    """Compatibility decorator for Python 2/3 string handling"""
    return klass
encoding.python_2_unicode_compatible = python_2_unicode_compatible

from django.utils import datastructures
from collections import OrderedDict
class SortedDict(OrderedDict):
    """Compatibility class for older Django code"""
    def __new__(cls, *args, **kwargs):
        instance = super(SortedDict, cls).__new__(cls, *args, **kwargs)
        instance.keyOrder = []
        return instance
    def __init__(self, data=None):
        super(SortedDict, self).__init__()
        if data:
            self.update(data)
datastructures.SortedDict = SortedDict

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='your-secret-key-here')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])

# Application definition
INSTALLED_APPS = [
    # Local apps - common must be first for compatibility layers
    'condottieri_common',

    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # Third party apps
    'allauth',  # django-allauth
    'allauth.account',  # django-allauth account
    'allauth.socialaccount',  # django-allauth social account
    'avatar',  # django-avatar
    'notifications',  # django-notifications-hq
    'django_pagination_bootstrap',  # django-pagination-bootstrap
    'transmeta',
    'django_messages',  # Required by condottieri_messages
    'crispy_forms',  # django-crispy-forms
    'crispy_bootstrap4',  # django-crispy-forms bootstrap4
    
    # Local apps
    'condottieri_profiles',
    'condottieri_messages',
    'condottieri_events',
    'condottieri_scenarios',
    'machiavelli',
]

# Crispy Forms settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_pagination_bootstrap.middleware.PaginationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            '/home/jonmarkgo/.local/share/mise/installs/python/3.11.11/lib/python3.11/site-packages/crispy_forms/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

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
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Scenarios
SCENARIOS_ROOT = 'scenarios'

# Maps
MAPS_ROOT = os.path.join('static', 'machiavelli', 'img')

# Auth settings
AUTH_PROFILE_MODULE = 'condottieri_profiles.CondottieriProfile'
LOGIN_REDIRECT_URL = 'machiavelli:summary'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Sites framework
SITE_ID = 1

# Import karma settings
from .karma import *

# Authentication
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'machiavelli:summary'
LOGOUT_REDIRECT_URL = 'machiavelli:summary'

# Django AllAuth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'
ACCOUNT_ADAPTER = 'allauth.account.adapter.DefaultAccountAdapter'
ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_USERNAME_MIN_LENGTH = 1
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_RATE_LIMITS = {
    'login_failed': '5/5m',  # 5 attempts per 5 minutes
}
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_SESSION_REMEMBER = None
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_REDIRECT_URL = 'machiavelli:summary'

# Profile settings
SIGNATURE_MAX_LENGTH = 1024  # Maximum length for user signatures
KARMA_DEFAULT = 100  # Default karma for new users
KARMA_MAXIMUM = 200  # Maximum karma a user can have
KARMA_MINIMUM = 10  # Minimum karma a user can have
KARMA_TO_JOIN = 50  # Minimum karma required to join a game
KARMA_TO_FAST = 75  # Minimum karma required to join a fast game
KARMA_TO_PRIVATE = 100  # Minimum karma required to create a private game
KARMA_TO_UNLIMITED = 200  # Minimum karma required to play unlimited games
GAMES_LIMIT = 3  # Maximum number of games a user can play simultaneously
SURRENDER_KARMA = -10  # Karma penalty for surrendering
DEFAULT_AUTOSUBSCRIBE = True  # Automatically subscribe to topics that you answer

# Game settings
BONUS_TIME = 0.2  # Percentage of time limit when karma bonus is awarded

# Authentication settings
LOGIN_REDIRECT_URLNAME = "machiavelli:summary"

# Clones detection
IP_HEADER = env('IP_HEADER', default='HTTP_X_FORWARDED_FOR')

# Notification settings
NOTIFICATION_QUEUE_ALL = env.bool('NOTIFICATION_QUEUE_ALL', default=True)

# Cache settings
CACHE_BACKEND = env('CACHE_BACKEND', default='locmem://')

# Django Notifications
DJANGO_NOTIFICATIONS_CONFIG = {
    'USE_JSONFIELD': True,
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Site ID
SITE_ID = 1

# CSRF and Security settings
CSRF_TRUSTED_ORIGINS = [
    'https://local.jonmarkgo.com',
    'http://local.jonmarkgo.com',
    'https://local.jonmarkgo.com:443',
    'http://local.jonmarkgo.com:80',
    'http://3018local:8000'
]
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = 'local.jonmarkgo.com'
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# Session settings
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_DOMAIN = 'local.jonmarkgo.com'

# Security settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# ... existing code ... 