"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import sentry_sdk
import django.db.models.signals
from socket import gethostname, gethostbyname
from pathlib import Path
from config import djsettings
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = djsettings.SECRET_KEY

ALLOWED_HOSTS = djsettings.get("ALLOWED_HOSTS", cast="@str").split(",")
ALLOWED_HOSTS.append(gethostbyname(gethostname()))

BASE_URL = djsettings.get("BASE_URL", cast="@str")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = djsettings.get("DEBUG", False, cast="@bool")
ENVIRONMENT = djsettings.ENVIRONMENT

CALENDAR_NAME_PREFIX = djsettings.get('CALENDAR_NAME_PREFIX', '', cast="@str")


AUTH_USER_MODEL = "users.User"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    # "corsheaders",
    "core",
    "users",
]

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "core.middleware.CustomCorsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "webapp.urls"

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

WSGI_APPLICATION = "webapp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if ENVIRONMENT == "dev":
    DATABASES = {
        "default": {
            "ENGINE": djsettings.DATABASES__default__ENGINE,
            "NAME": djsettings.DATABASES__default__NAME,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": djsettings.DATABASES__default__ENGINE,
            "NAME": djsettings.DATABASES__default__NAME,
            "USER": djsettings.DATABASES__default__USER,
            "PASSWORD": djsettings.DATABASES__default__PASSWORD,
            "HOST": djsettings.DATABASES__default__HOST,
            "PORT": djsettings.DATABASES__default__PORT,
            # "OPTIONS": json.loads(djsettings.DATABASES__default__OPTIONS),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Bahia"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]

STATIC_URL = "static/"
STATIC_ROOT = "static"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
CSRF_TRUSTED_ORIGINS = [BASE_URL]

sentry_sdk.init(
    dsn="https://e19909e9414044d9981111c4b4acdf30@app.glitchtip.com/6805",
    environment=ENVIRONMENT,
    integrations=[
        DjangoIntegration(
            transaction_style='url',
            middleware_spans=True,
            signals_spans=True,
            signals_denylist=[
                django.db.models.signals.pre_init,
                django.db.models.signals.post_init,
            ],
            cache_spans=False,
        ),
    ],
)
