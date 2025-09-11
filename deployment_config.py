"""
Deployment configuration to explicitly specify settings module
"""
import os
import sys

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Explicitly set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobland.settings')

# Import Django and configure
import django
from django.conf import settings

if not settings.configured:
    django.setup()
