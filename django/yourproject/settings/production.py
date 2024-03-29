# Parse database configuration from $DATABASE_URL
import dj_database_url
from os import environ

from .base import *

ALLOWED_HOSTS = ['yourproject.example.com']

DATABASES = {
    'default': dj_database_url.config()
}
STATIC_ROOT= '/home/ubuntu/static'
#STATIC_ROOT = os.environ.get('STATIC_ROOT')
