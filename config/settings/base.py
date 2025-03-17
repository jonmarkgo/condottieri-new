"""
Base settings for Condottieri project.
"""
import os
from pathlib import Path
import environ

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
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'modeltranslation',  # Must be before django.contrib.admin
    'debug_toolbar',
    'crispy_forms',
    'django_pagination_bootstrap',
    'notifications',
    'mailer',
    'markdownx',
    'widget_tweaks',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'avatar',  # User avatars
]

LOCAL_APPS = [
    'machiavelli',
    'condottieri_profiles',
    'condottieri_messages',
    'condottieri_events',
    'condottieri_common',
    'condottieri_scenarios',
    'condottieri_notification',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'machiavelli.context_processors.games',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres:///condottieri')
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# django-modeltranslation settings
gettext = lambda s: s
LANGUAGES = [
    ('en', gettext('English')),
    ('es', gettext('Spanish')),
    ('it', gettext('Italian')),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'es', 'it')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('en', 'es', 'it')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Scenarios
SCENARIOS_ROOT = 'machiavelli'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Email configuration
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Django AllAuth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'

# Django Notifications
DJANGO_NOTIFICATIONS_CONFIG = {
    'USE_JSONFIELD': True,
}

# Site ID
SITE_ID = 1

# Profile settings
SIGNATURE_MAX_LENGTH = 1024  # Maximum length for user signatures
KARMA_DEFAULT = 100  # Default karma for new users
KARMA_MAXIMUM = 1000  # Maximum karma a user can have
KARMA_MINIMUM = 0  # Minimum karma a user can have
KARMA_TO_JOIN = 50  # Minimum karma required to join a game
KARMA_TO_FAST = 75  # Minimum karma required to join a fast game
KARMA_TO_PRIVATE = 100  # Minimum karma required to create a private game
KARMA_TO_UNLIMITED = 200  # Minimum karma required to play unlimited games
GAMES_LIMIT = 3  # Maximum number of games a user can play simultaneously
SURRENDER_KARMA = -10  # Karma penalty for surrendering
DEFAULT_AUTOSUBSCRIBE = True  # Automatically subscribe to topics that you answer 