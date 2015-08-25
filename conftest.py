import tempfile

from django.conf import settings


def pytest_configure():
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'NAME': 'youtube_thumbnail',
                'TEST_NAME': 'youtube_thumbnail_test',
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.admin',
            'youtube_thumbnail',
        ),
        TEMPLATE_DIRS=(
            tempfile.gettempdir(),
        ),
        CACHES={
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            }
        },
    )
