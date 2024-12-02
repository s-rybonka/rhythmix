from factory import DjangoModelFactory
from factory import Faker

from songs import models as songs_models


class SongFactory(DjangoModelFactory):
    title = Faker('name')
    author = Faker('name')

    class Meta:
        model = songs_models.Song
