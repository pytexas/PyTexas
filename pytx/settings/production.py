import os

import dj_database_url

from pytx.release import RELEASE

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

from pytx.settings.base import *

SECURE_SSL_REDIRECT = False

BASE_URL = 'https://www.pytexas.org'

RAVEN_CONFIG = {
    'dsn': os.environ.get('RAVEN_BACKEND', None),
    'release': RELEASE,
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = 'pytexas'
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = 'public-read'

DATABASES = {
    # 'backup': {
    #     'ENGINE': 'zappa_django_utils.db.backends.s3sqlite',
    #     'NAME': 'db.sqlite3',
    #     'BUCKET': 'pytexasdb'
    # }
}

DATABASES['default'] = dj_database_url.config(
    default='postgres://localhost:5432/pytexas')
