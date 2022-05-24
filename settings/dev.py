"""Development settings and globals."""

from fnmatch import fnmatch
from os.path import join, normpath
from socket import gethostbyname, gethostname

from settings.common import *

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
########## END EMAIL CONFIGURATION


########## TOOLBAR CONFIGURATION
INSTALLED_APPS += (
    "debug_toolbar",
    "django_extensions",
)
MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
########## END TOOLBAR CONFIGURATION
