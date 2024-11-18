# from .base import *
from . import *  # noqa
# SECURITY WARNING: don't run with debug turned on in production!
import os

from .__init__ import *
SECRET_KEY =os.getenv("DJANGO_SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"