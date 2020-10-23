import os
from tempfile import mkdtemp

from django import setup
from django.conf import settings


def pytest_configure():
    """
    Configuration for test.
    """
    settings.configure(
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        DATABASES={
            "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
        },
        SECRET_KEY=os.urandom(24),
        USE_I18N=True,
        USE_L10N=True,
        ROOT_URLCONF="accounts.urls",
        MIDDLEWARE=(
            "django.middleware.common.CommonMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
        ),
        INSTALLED_APPS=(
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.sites",
            "django.contrib.staticfiles",
            "rest_framework",
            "rest_framework.authtoken",
            "accounts",
        ),
        PASSWORD_HASHERS=("django.contrib.auth.hashers.MD5PasswordHasher",),
        AUTH_USER_MODEL="accounts.User",
        MEDIA_ROOT=mkdtemp(),
    )
    setup()
