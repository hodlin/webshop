import os
from celery import Celery
from django.conf import settings

# Set the default Django setting module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webshop.settings')

app = Celery('webshop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
