import pytest
from django.conf import settings as dj_settings


def pytest_configure():
    dj_settings.ALLOWED_HOSTS = ['*']


@pytest.fixture(autouse=True)
def enable_db(db):
    pass
