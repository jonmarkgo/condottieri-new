import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

print("Python path:", sys.path)
print("Current directory:", os.getcwd())

# Import base settings
from config.settings.base import *

# Override settings for debugging
DEBUG = True
SECRET_KEY = 'django-insecure-development-key-change-this-in-production'
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debug toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1']

# Scenarios
SCENARIOS_ROOT = 'scenarios'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'debug_settings')

from django.conf import settings
print("\nDjango settings:")
print("DATABASES setting:", settings.DATABASES)
print("BASE_DIR:", settings.BASE_DIR)
print("Settings module:", os.environ.get('DJANGO_SETTINGS_MODULE'))
print("Installed apps:", settings.INSTALLED_APPS) 