import os
from blackend.__settings__.back_compatibility import *

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = PACKAGE_ROOT

DEBUG = True


# Local Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
    }
}



ALLOWED_HOSTS = ["*"]

# Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "UTC"
# For languages http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"
SITE_ID = int(os.environ.get("SITE_ID", 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If False, Django will not use timezone-aware datetimes.
USE_TZ = True


# For img, videos
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")
MEDIA_URL = "/site_media/media/"


# For css,js,less https://docs.djangoproject.com/en/1.9/ref/contrib/staticfiles/
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")
STATIC_URL = "/site_media/static/"
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static", "dist"),
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

SECRET_KEY = open(os.path.join(PROJECT_ROOT,"keys.txt")).read()

# TEMPLATE_CONTEXT_PROCESSORS = ["account.context_processors.account",
#                                 "django.core.context_processors.request"]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PACKAGE_ROOT, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "pinax_theme_bootstrap.context_processors.theme",
                'django.template.context_processors.request',
            ],
        },
    },
]



MIDDLEWARE_CLASSES = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "account.middleware.LocaleMiddleware",
    "account.middleware.TimezoneMiddleware",
]

ROOT_URLCONF = "blackend.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "blackend.wsgi.application"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    


    # app
    "account",
    # "authsocial",

    # theme and dependencies
    "bootstrapform",
    "pinax_theme_bootstrap",
    "debug_toolbar",

    # project
    "blackend",
]







# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# SOcial authentication settings

# AUTHENTICATION_BACKENDS = [
#     'social_auth.backends.twitter.TwitterBackend',
#     'social_auth.backends.facebook.FacebookBackend',
#     'social_auth.backends.google.GoogleOAuthBackend',
#     'social_auth.backends.google.GoogleOAuth2Backend',
#     'social_auth.backends.google.GoogleBackend',
#     'social_auth.backends.browserid.BrowserIDBackend',
#     'social_auth.backends.contrib.linkedin.LinkedinBackend',
#     'social_auth.backends.contrib.github.GithubBackend',
#     'social_auth.backends.OpenIDBackend',
#     'django.contrib.auth.backends.ModelBackend',
# ]

# SOCIAL_AUTH_PIPELINE = [
#     "social.pipeline.social_auth.social_details",
#     "social.pipeline.social_auth.social_uid",
#     "social.pipeline.social_auth.auth_allowed",
#     "social.pipeline.social_auth.social_user",
#     "social.pipeline.user.get_username",
#     "authsocial.pipeline.prevent_dupes",
#     "social.pipeline.user.create_user",
#     "social.pipeline.social_auth.associate_user",
#     "social.pipeline.social_auth.load_extra_data",
#     "social.pipeline.user.user_details"
# ]

# SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/"

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ""
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ""
# SOCIAL_AUTH_TWITTER_KEY = ""
# SOCIAL_AUTH_TWITTER_SECRET = ""
# SOCIAL_AUTH_FACEBOOK_KEY = ""
# SOCIAL_AUTH_FACEBOOK_SECRET = ""

# SOCIAL_AUTH_FACEBOOK_SCOPE = [
#     "email"
# ]
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
#     "profile",
#     "email"
# ]
