"""Production settings and globals."""


import re
from os import environ

import sentry_sdk

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured
from sentry_sdk.integrations.django import DjangoIntegration

from settings.common import *


def get_env_setting(setting):
    """Get the environment setting or return exception"""
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


INSTALLED_APPS = ("corsheaders",) + INSTALLED_APPS + ("gunicorn",)

########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = get_env("ALLOWED_HOSTS").split(",")
########## END HOST CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get("EMAIL_HOST", "smtp.gmail.com")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get("EMAIL_HOST_PASSWORD", "")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get("EMAIL_HOST_USER", "your_email@example.com")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get("EMAIL_PORT", 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = "[%s] " % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting("SECRET_KEY")
########## END SECRET CONFIGURATION


########## SENTRY CONFIGURATION
sentry_sdk.init(
    dsn=get_env("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
########## END SENTRY CONFIGURATION

######### CORSHEADERS CONFIGURATION
CSRF_TRUSTED_ORIGINS = get_env("CSRF_TRUSTED_ORIGINS").split(",")
CSRF_COOKIE_DOMAIN = get_env("CSRF_COOKIE_DOMAIN")
CORS_ORIGIN_REGEX_WHITELIST = [
    re.compile(r) for r in get_env("CORS_ORIGIN_REGEX_WHITELIST").split(",")
]
CORS_REPLACE_HTTPS_REFERER = True
CORS_ALLOW_CREDENTIALS = True
CORS_URLS_REGEX = re.compile(get_env("CORS_URLS_REGEX"))
CSRF_COOKIE_SAMESITE = get_env("CSRF_COOKIE_SAMESITE")
SESSION_COOKIE_SAMESITE = get_env("SESSION_COOKIE_SAMESITE")
######### END CORSHEADERS CONFIGURATION
DEBUG = get_env("DEBUG") == "True"

MIDDLEWARE += ("corsheaders.middleware.CorsMiddleware",)
