from factory import DjangoModelFactory
from factory import Faker
from factory import PostGenerationMethodCall


USER_PASSWORD = '12345Qwerty'


class UserFactory(DjangoModelFactory):
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    password = PostGenerationMethodCall('set_password', USER_PASSWORD)

    class Meta:
        model = 'users.User'
