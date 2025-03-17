import os
import sys

print("Python path:", sys.path)
print("Current directory:", os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from django.conf import settings
print("\nDjango settings:")
print("DATABASES setting:", settings.DATABASES)
print("BASE_DIR:", settings.BASE_DIR)
print("Settings module:", os.environ.get('DJANGO_SETTINGS_MODULE'))
print("Installed apps:", settings.INSTALLED_APPS) 