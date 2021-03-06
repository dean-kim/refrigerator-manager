"""
Django settings for refrigerator_manager project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

from .base import *


# DEBUG
# ------------------------------------------------------------------------------
#DEBUG = env.bool('DJANGO_DEBUG', default=True)

DEBUG = False

SECRETS_DIR = ROOT_DIR.path('.secrets')

SECRETS_BASE = SECRETS_DIR.path('secrets.json')

with open(".secrets/secrets.json") as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError: # pragma: no cover
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')

sys.path.insert(0, path.abspath(APPS_DIR()))

env = environ.Env()

SETTING_TYPE = 'Common'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'refrigeratordb',
        'USER': get_secret("AWS_RDS_DB_USER_NAME"),
        'PASSWORD': get_secret("AWS_RDS_DB_PASSWORD"),
        'HOST': 'refrigeratordb.cxxu9sutjmtm.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = '*'

###
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'zappa-xbm6fu5jw'
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Static Setting
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_STORAGE_BUCKET_NAME = 'zappa-xbm6fu5jw'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


