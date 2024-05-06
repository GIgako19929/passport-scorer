"""
Django settings for scorer project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from datetime import timedelta

from .env import BASE_DIR, env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=True)

ALLOWED_HOSTS = env.json("ALLOWED_HOSTS", default=[])

CERAMIC_CACHE_API_KEY = env("CERAMIC_CACHE_API_KEY", default="")

UI_DOMAINS = env("UI_DOMAINS", default=["localhost:3000", "www.localhost:3000"])

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env("GOOGLE_OAUTH_CLIENT_ID", default="")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env("GOOGLE_CLIENT_SECRET", default="")

SECURE_SSL_REDIRECT = env("SECURE_SSL_REDIRECT", default=False)
SECURE_PROXY_SSL_HEADER = env.json("SECURE_PROXY_SSL_HEADER", default=None)

UPTIME_ROBOT_READONLY_API_KEY = env("UPTIME_ROBOT_READONLY_API_KEY", default="")
# comma separated list of urls to ignore
IGNORE_UNMONITORED_URLS = env("IGNORE_UNMONITORED_URLS", default="")

STAKING_SUBGRAPH_API_KEY = env("STAKING_SUBGRAPH_API_KEY", default="api-key")

GENERIC_COMMUNITY_CREATION_LIMIT = env.int(
    "GENERIC_COMMUNITY_CREATION_LIMIT", default=5
)

USER_COMMUNITY_CREATION_LIMIT = env.int("USER_COMMUNITY_CREATION_LIMIT", default=5)

FF_API_ANALYTICS = env("FF_API_ANALYTICS", default="Off")
LOGGING_STRATEGY = env(
    "LOGGING_STRATEGY", default="default"
)  # default | structlog_json | structlog_flatline

LOGIN_REDIRECT_URL = "/admin"

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
    "scorer.pipeline.add_social_auth_user_to_group",
)

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "rest_framework_api_key",
    "registry",
    "scorer_apu",
    "scorer_weighted",
    "stake",
    "ceramic_cache",
    "corsheaders",
    "account",
    "ninja_extra",
    "social_django",
    "passport_admin",
    # "debug_toolbar",
    "cgrants",
    "django_filters",
    "trusta_labs",
    "tos",
    "django_ace",
    "data_model",
]

AUTHENTICATION_BACKENDS = [
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "scorer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "./scorer/templates"),
        ],
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

WSGI_APPLICATION = "scorer.wsgi.application"


CSRF_TRUSTED_ORIGINS = env.json("CSRF_TRUSTED_ORIGINS", default=[])

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": env.db(default="sqlite:///db.sqlite3"),
    "data_model": env.db(
        "DATA_MODEL_DATABASE_URL", default="sqlite:///db_data_model.sqlite3"
    ),
    "read_replica_0": {
        **env.db_url("READ_REPLICA_0_URL", default="sqlite:///db.sqlite3"),
        "TEST": {"MIRROR": "default"},
    },
}

DATABASE_ROUTERS = ["scorer.db_router.ScorerRouter"]

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

LOG_SQL_QUERIES = env("LOG_SQL_QUERIES", default=False)


CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "x-api-key",
]

if LOGGING_STRATEGY in ("structlog_json", "structlog_flatline"):
    import structlog

    MIDDLEWARE += ["django_structlog.middlewares.RequestMiddleware"]

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json_formatter": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.processors.JSONRenderer(),
            },
            "plain_console": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.dev.ConsoleRenderer(),
            },
            "key_value": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.processors.KeyValueRenderer(
                    key_order=["timestamp", "level", "event", "logger"]
                ),
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": (
                    "json_formatter"
                    if LOGGING_STRATEGY == "structlog_json"
                    else "plain_console"
                ),
            },
            # "json_file": {
            #     "class": "logging.handlers.WatchedFileHandler",
            #     "filename": "logs/json.log",
            #     "formatter": "json_formatter",
            # },
            # "flat_line_file": {
            #     "class": "logging.handlers.WatchedFileHandler",
            #     "filename": "logs/flat_line.log",
            #     "formatter": "key_value",
            # },
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "loggers": {
            "django_structlog": {
                "handlers": [],
                "level": "DEBUG",
                "propagate": True,
            },
            "django": {
                "level": "DEBUG",
                "handlers": [],
                "propagate": False,
            },
            "django.db.backends": {
                "level": "DEBUG",
                "handlers": [],
                "propagate": False,
            },
        },
    }

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.filter_by_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

else:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "rootFormatter": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(thread)d - %(pathname)s:%(lineno)d %(message)s",
            }
        },
        "filters": {
            "require_debug_true": {
                "()": "django.utils.log.RequireDebugTrue",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "rootFormatter",
            },
            "debugConsole": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "filters": ["require_debug_true"],
                "formatter": "rootFormatter",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "loggers": {
            "django": {
                "level": "DEBUG",
                "handlers": [],
                "propagate": False,
            },
            "django.db.backends": {
                "level": "DEBUG",
                "handlers": ["debugConsole"] if LOG_SQL_QUERIES else [],
                "propagate": False,
            },
            "urllib3": {
                "level": "DEBUG",
                "handlers": [],
                "propagate": False,
            },
            "botocore": {
                "level": "DEBUG",
                "handlers": [],
                "propagate": False,
            },
        },
    }


STATIC_ROOT = BASE_DIR / "static"


NINJA_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "ninja_jwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("ninja_jwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "ninja_jwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

TEST_MNEMONIC = env("TEST_MNEMONIC")


CERAMIC_CACHE_CACAO_VALIDATION_URL = env(
    "CERAMIC_CACHE_CACAO_VALIDATION_URL", default="http://127.0.0.1:8001/verify"
)

MAX_BULK_CACHE_SIZE = 100

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": env("CELERY_BROKER_URL", default="redis://localhost:6379/0"),
    }
}

CERAMIC_CACHE_SCORER_ID = env("CERAMIC_CACHE_SCORER_ID")
CERAMIC_CACHE_CONVERT_STAMP_TO_V2_URL = env(
    "CERAMIC_CACHE_CONVERT_STAMP_TO_V2_URL",
    default="http://localhost:8003/api/v0.0.0/convert",
)

PASSPORT_PUBLIC_URL = env("PASSPORT_PUBLIC_URL", default="http://localhost:80")

# Deprecated in favour of TRUSTED_IAM_ISSUERS which will store a list of trusted issuers
TRUSTED_IAM_ISSUER = env(
    "TRUSTED_IAM_ISSUER", default="did:key:GlMY_1zkc0i11O-wMBWbSiUfIkZiXzFLlAQ89pdfyBA"
)
TRUSTED_IAM_ISSUERS = env.json(
    "TRUSTED_IAM_ISSUERS",
    default=["did:key:GlMY_1zkc0i11O-wMBWbSiUfIkZiXzFLlAQ89pdfyBA"],
)


CGRANTS_API_TOKEN = env("CGRANTS_API_TOKEN", default="abc")

IPWARE_META_PRECEDENCE_ORDER = (
    "X_FORWARDED_FOR",
    "HTTP_X_FORWARDED_FOR",  # <client>, <proxy1>, <proxy2>
    "HTTP_CLIENT_IP",
    "HTTP_X_REAL_IP",
    "HTTP_X_FORWARDED",
    "HTTP_X_CLUSTER_CLIENT_IP",
    "HTTP_FORWARDED_FOR",
    "HTTP_FORWARDED",
    "HTTP_VIA",
    "REMOTE_ADDR",
)

RESCORE_QUEUE_URL = env("RESCORE_QUEUE_URL", default="")

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
