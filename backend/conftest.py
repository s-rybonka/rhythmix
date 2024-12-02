import pytest
from django.conf import settings as dj_settings
from rest_framework.test import APIClient

from users.tests import factories as users_factories


def pytest_configure():
    dj_settings.ALLOWED_HOSTS = ['*']


@pytest.fixture(autouse=True)
def enable_db(db):
    pass


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return users_factories.UserFactory(email='user@rhythmix.fun')
