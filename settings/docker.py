from .base import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'studydb'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', '123'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
        'ATOMIC_REQUESTS': True
    }
}

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-kh%z9jz66va7zjb9w%qelhnfubcic^0zk(ie_#dk=72l+1r=rj')

MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
