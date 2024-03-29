# -*- coding: utf-8 -*-
"""
Django settings for saas_app project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import sys
import os
import environ

ROOT_DIR = (
    environ.Path(__file__) - 3
)  # (saas_app/config/settings/common.py - 3 = saas_app/)
APPS_DIR = ROOT_DIR.path("saas_app")

env = environ.Env()

# APP CONFIGURATION
# -------------------------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Useful template tags:
    "django.contrib.humanize",
    # Admin
    "django.contrib.admin",
)
THIRD_PARTY_APPS = (
    "bootstrap5",  # bootstrap 5
    "crispy_forms",  # Form layouts
    "crispy_bootstrap5",
    "allauth",  # registration
    "allauth.account",  # registration
    "allauth.socialaccount",  # registration
    "allauth.socialaccount.providers.stripe",  # stripe registration
    "saas_app.taskapp.celery.CeleryConfig",  # celery
    "compressor",  # django-compressor
    "djcelery_email",  # send mails through as celery task
    "loginas",  # allows login as user
    "webpack_loader",  # webpack loader for react
    "rest_framework",  # REST API
    "graphene_django",  # Required for GraphiQL
    "tinymce",  # django-tinymce, used for the blog
    "djstripe",  # payment-plans
)

# Apps specific for this project go here.
LOCAL_APPS = (
    "saas_app.users",
    "saas_app.app",
    "saas_app.api",
    # 'saas_app.payments',
    "saas_app.blog",
    "saas_app.beta",
    # Your stuff: custom apps go here
    #'saas_app.users.apps.UsersConfig'
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# -------------------------------------------------------------------------------------------------
MIDDLEWARE = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

# MIGRATIONS CONFIGURATION
# -------------------------------------------------------------------------------------------------
MIGRATION_MODULES = {"sites": "saas_app.contrib.sites.migrations"}

# DEBUG
# -------------------------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", True)

# FIXTURE CONFIGURATION
# -------------------------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (str(APPS_DIR.path("fixtures")),)

# EMAIL CONFIGURATION
# -------------------------------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="djcelery_email.backends.CeleryEmailBackend"
)
EMAIL_SUBJECT_PREFIX = ""

# MANAGER CONFIGURATION
# -------------------------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (("""Angel Vargas""", "angel@saasapp.io"),)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# -------------------------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    "default": env.db(
        "DATABASE_URL",
        default="postgres://{user}:{password}@postgres:5432/{user}".format(
            user=env("POSTGRES_USER"), password=env("POSTGRES_PASSWORD", default="")
        ),
    ),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True


# GENERAL CONFIGURATION
# -------------------------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "UTC"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-gb"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# -------------------------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [
            str(APPS_DIR.path("templates")),
        ],
        "OPTIONS": {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            "debug": DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# STATIC FILE CONFIGURATION
# -------------------------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR("staticfiles"))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (str(APPS_DIR.path("static")),)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",  # django-compressor
)

# MEDIA CONFIGURATION
# -------------------------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# URL CONFIGURATION
# -------------------------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"

# WSGI CONFIGURATION
# -------------------------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# ADMIN CONFIGURATION
# -------------------------------------------------------------------------------------------------
# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r"^admin/"

# AUTHENTICATION CONFIGURATION
# -------------------------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "app:dashboard"
LOGIN_URL = "account_login"

# DJANGO-ALLAUTH CONFIGURATION
# -------------------------------------------------------------------------------------------------
# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_SIGNUP_FORM_CLASS = "saas_app.users.forms.MyUserCreationForm"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USER_DISPLAY = lambda u: u.email
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""

ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_ADAPTER = "saas_app.users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "saas_app.users.adapters.SocialAccountAdapter"

# CELERY CONFIGURATION
# -------------------------------------------------------------------------------------------------
BROKER_URL = env(
    "CELERY_BROKER_URL", default=env("REDIS_URL", default="redis://redis:6379")
)
CELERY_RESULT_BACKEND = BROKER_URL

# CACHE CONFIGURATION
# -------------------------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL", default="redis://redis:6379"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,  # mimics memcache behavior.
            # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
        },
    }
}


# DJANGO-CRISPY-FORMS CONFIGURATION
# -------------------------------------------------------------------------------------------------
# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# OCTOBAT CONFIGURATION
# -------------------------------------------------------------------------------------------------
OCTOBAT_SUPPLIER_NAME = "saasapp.io"


# SAAS CONFIGURATION
# -------------------------------------------------------------------------------------------------
# This email receives info mails once a new account is created, or a user requests an invite to
# the site (if in private beta mode).
SAAS_INFO_MAIL = "info@saasapp.io"


# Setting `SAAS_PRIVATE_BETA` to True sets the page in private beta mode:
# - The default user registration is blocked
# - Users interested in the private beta can request an invite
# - Invites are managed through the admin interface
# - Only users with an invite can create a new account
SAAS_PRIVATE_BETA = False


# The `SAAS_SUBSCRIPTION_TYPE` sets the default plan for new users. Allowed values are:
# - freemium: The user is subscribed to a free plan that never expires.
# - trial: The user is subscribed to a trial plan that expires after `SAAS_TRIAL_LENGTH` which
#          defaults to 14 days.
# - None: The user is not subscribed to any plan and has to subscribe to a paid plan.
SAAS_SUBSCRIPTION_TYPE = "freemium"


SAAS_PLANS = {
    # This is the free plan. Every new user will be subscribed to this plan automatically if you
    # set `SAAS_SUBSCRIPTION_TYPE` to `freemium`.
    "free": {
        "description": "Basic Plan Description",
        "features": [
            "Feature 1",
            "Feature 2",
        ],
    },
    "freemium": {
        "description": "Free Plan Description",
        "features": [
            "Mail campaings management",
        ],
        "testfield": ["something"],
    },
    # Custom plans go here.
    # ---------------------
    # To add a new plan, log into your stripe account and create a new plan.
    # Once created, run:
    #     docker-compose run django python manage.py sync_plans
    # and add the plan here.
    # The key is the plan id, so a plan with the id `basic` would look like this:
    # "basic": {
    #    "description": "Basic Plan Description",
    #    "features": [
    #        "Feature 1",
    #        "Feature 2",
    #    ]
    # },
    "basic": {
        "description": "Basic Plan Description",
        "features": [
            "Feature 1",
            "Feature 2",
        ],
    },
}


# WEBPACK CONFIGURATION
# -------------------------------------------------------------------------------------------------
STATS_FILE = ROOT_DIR("webpack-stats.json")
WEBPACK_LOADER = {"DEFAULT": {"STATS_FILE": STATS_FILE}}

# DJANGORESTFRAMEWORK CONFIGURATION
# -------------------------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 15,
}


# TESTING CONFIGURATION
# -------------------------------------------------------------------------------------------------
if "test" in sys.argv:
    CELERY_ALWAYS_EAGER = True

# Your common stuff: Below this line define 3rd party library settings

# GraphQL
GRAPHENE = {"SCHEMA": "saas_app.schemas.graphql.schema"}

# Stripe
STRIPE_LIVE_SECRET_KEY = os.environ.get(
    "STRIPE_LIVE_SECRET_KEY",
    "sk_test_51JtF4KFDRKyuJLcBh7Ce0ofrcnC4AyeMa4AGjKCP7iSRfKyHQA1Kp174XkDfROrDRHquCH8OE5R5yHeqULFPlySz00jch9Piv0",
)
STRIPE_TEST_SECRET_KEY = os.environ.get(
    "STRIPE_TEST_SECRET_KEY",
    "sk_test_51JtF4KFDRKyuJLcBh7Ce0ofrcnC4AyeMa4AGjKCP7iSRfKyHQA1Kp174XkDfROrDRHquCH8OE5R5yHeqULFPlySz00jch9Piv0",
)
STRIPE_LIVE_MODE = False  # Change to True in production
DJSTRIPE_WEBHOOK_SECRET = "whsec_xxx"  # Get it from the section in the Stripe dashboard where you added the webhook endpoint
DJSTRIPE_USE_NATIVE_JSONFIELD = (
    True  # We recommend setting to True for new installations
)
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"
# Your local stuff: Below this line define 3rd party library settings
# STRIPE_API_VERSION = "2020-08-27"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
