"""Common settings and globals."""


from datetime import timedelta
from os.path import abspath, basename, dirname, join, normpath
from pathlib import Path
from sys import path

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

from settings.utils import get_env

########## PATH CONFIGURATION
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Absolute filesystem path to the project directory:
PROJECT_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level package folder:
PACKAGE_ROOT = dirname(PROJECT_ROOT)

# .env file path
env_path = Path(PROJECT_ROOT) / ".env"

######### .ENV CONFIGURATION
load_dotenv(dotenv_path=env_path)
######### END .ENV CONFIGURATION

# Site name:
SITE_NAME = get_env("SITE_NAME")
SITE_ID = int(get_env("SITE_ID"))

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(PACKAGE_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = get_env("DEBUG") == "True"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## CACHE CONFIGURATION
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": get_env("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
########## END CACHE CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": get_env("DEFAULT_DATABASE_NAME"),
        "USER": get_env("DEFAULT_DATABASE_USER"),
        "PASSWORD": get_env("DEFAULT_DATABASE_PASSWORD"),
        "HOST": get_env("DEFAULT_DATABASE_HOST"),
        "PORT": get_env("DEFAULT_DATABASE_PORT"),
    }
}
########## END DATABASE CONFIGURATION


########## PASSWORD CONFIGURATION
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
########## END PASSWORD CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = "UTC"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = get_env("LANGUAGE_CODE")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = get_env("MEDIA_ROOT")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = get_env("MEDIA_URL")
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = get_env("STATIC_ROOT")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = get_env("STATIC_URL")
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = "5z1qxhko4@0bd^7kzxp31&vl$5rdfl@dv!se8(&gale1k***&u"
########## END SECRET CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = get_env("ALLOWED_HOSTS").split(",")
ALLOWED_HOSTS = []
DEFAULT_DOMAIN = get_env("DEFAULT_DOMAIN")
########## END SITE CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
# FIXTURE_DIRS = (Path(join(PROJECT_ROOT, "fixtures")),)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE = (
    # Default Django middleware.
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "src.core.urls"
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Useful template tags:
    # 'django.contrib.humanize',
    # this sould be before admin
    # "modeltranslation",
    # Admin panel and documentation:
    "django.contrib.admin",
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    "rest_framework",
    "tinymce",
    "django_elasticsearch_dsl",
)

# Apps specific for this project go here.
LOCAL_APPS = (
    "src.api",
    "src.apps.authentication",
    "src.apps.storage",
    "src.apps.notifications",
    "src.apps.blog",
    "src.apps.events",
    "src.apps.terms",
    "src.apps.website",
    "src.apps.reservations",
    "src.apps.categories",
    "src.apps.polls",
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "src.core.wsgi.application"
########## END WSGI CONFIGURATION


########## AUTH USER MODEL CONFIGURATION
AUTH_USER_MODEL = "authentication.User"
########## END AUTH USER MODEL CONFIGURATION


########## NATS CONFIGURATION
NATS_CLUSTER_ID = get_env("NATS_CLUSTER_ID")
NATS_URL = get_env("NATS_URL")
########## END NATS CONFIGURATION


########## OTP CONFIGURATION
OTP_CODE_LENGTH = int(get_env("OTP_CODE_LENGTH"))
OTP_TTL = int(get_env("OTP_TTL"))
########## END OTP CONFIGURATION


########## RESTFARMEWORK CONFIGURATION
REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_RATES": {
        "otp_hour": get_env("OTP_HOUR"),
        "otp_day": get_env("OTP_DAY"),
    },
    "EXCEPTION_HANDLER": "src.api.exception_handler.api_exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "src.apps.authentication.backends.JWTAuthentication",
    ),
}
########## END RESTFARMEWORK CONFIGURATION
# ELASTICSEARCH CONFIGURATION
ELASTICSEARCH_DSL = {
    "default": {
        "hosts": get_env("ELASTICSEARCH_HOST"),
        "timeout": int(get_env("ELASTICSEARCH_TIMEOUT")),
        "use_ssl": False,
        "verify_certs": False,
    }
}
ELASTICSEARCH_INDEX_NAMES = {
    "src.apps.events.documents.event": "sutpe_events",
}
# END ELASTICSEARCH CONFIGURATION

########## JWT CONFIGURATION
ACCESS_TTL = int(get_env("ACCESS_TTL"))
REFRESH_TTL = int(get_env("REFRESH_TTL"))
JWT_SECRET = get_env("JWT_SECRET")
if (
    len(JWT_SECRET.encode("utf-8")) < 64
    or len(JWT_SECRET.encode("utf-8")) > 128
):
    raise ValueError("JWT_SECRET must be between 64 and 128 bytes")
########## END JWT CONFIGURATION

# DEVELOPMENT MODE CONFIGURATION
UNDER_DEVELOPMENT = get_env("UNDER_DEVELOPMENT", default="False") == "True"
# END DEVELOPMENT MODE CONFIGURATION
# PUSH NOTIF PROVIDER CONFIGURATION
PUSH_NOTIF_PROVIDER = get_env("PUSH_NOTIF_PROVIDER", default="PUSHE")
if PUSH_NOTIF_PROVIDER not in {"PUSHE", "FCM"}:
    raise ValueError("PUSH_NOTIF_PROVIDER must be PUSHE or FCM")
# END PUSH NOTIF PROVIDER CONFIGURATION
