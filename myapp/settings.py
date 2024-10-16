"""
Django settings for myapp project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
from environs import Env

#env = environ.FileAwareEnv(
#        DEBUG=(bool, False)
#)
#environ.Env.read_env()
#env = environ.Env(DEBUG=(bool, False))
#environ.Env.read_env()
env = Env()
env.read_env() 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-uwn-2-(t=#jz4les3n=ayf4)th@$vizvv-s1-sk&g#c=dj^m=t"

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = "DJANGO_DEBUG" in os.environ and os.environ["DJANGO_DEBUG"] == "ON"


ALLOWED_HOSTS = ['patraldo.dev', 'www.patraldo.dev', 'localhost', '127.0.0.1', 'poetry-django.fly.dev']  # <-- Updated!

CSRF_TRUSTED_ORIGINS = ['https://patraldo.dev', 'https://www.patraldo.dev', 'https://poetry-django.fly.dev']  # <-- Updated!


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework', # <-- here
    "myapp.spa", # <-- here
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # <-- here
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["myapp/templates"], # <-- here
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

WSGI_APPLICATION = "myapp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.sqlite3",
#        "NAME": BASE_DIR / "db.sqlite3",
#    }
#}
#DATABASES['default'] = dj_database_url.config(
#    default='sqlite:///db.sqlite3',
#    conn_max_age=600,
#    conn_health_checks=True,
#)
DATABASES = {
    'default': dj_database_url.config(
        #default='sqlite:///db.sqlite3', #local
        default='sqlite:////data/db.sqlite3', #production
        conn_max_age=600,
        conn_health_checks=True,
    )
}
#DATABASES = {
#   "default": env.dj_db_url("DATABASE_URL", default="sqlite:///db.sqlite3"),
#}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

#STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "myapp", "staticfiles")
STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "myapp", "static"),)

from django.urls import reverse_lazy

LOGIN_URL = reverse_lazy("login")
LOGIN_REDIRECT_URL = reverse_lazy("spa")
LOGOUT_REDIRECT_URL = reverse_lazy("spa")


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

logging_level = (
    "INFO" if "LOGGING_LEVEL" not in os.environ else os.environ["LOGGING_LEVEL"]
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "[%(asctime)s][%(levelname)8s][%(name)16.16s]@[%(lineno)5s]$ %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
        "propagate": False,
    },
    "loggers": {
        "django.server": {
            "level": "WARNING",
            "handlers": ["console"],
            "propagate": False,
        },
        "myapp": {
            "level": logging_level,
            "handlers": ["console"],
            "propagate": False,
        },
    },
}
