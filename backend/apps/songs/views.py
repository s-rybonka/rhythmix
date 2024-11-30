from rest_framework.viewsets import ModelViewSet

from songs import models as songs_models
from songs import serializers as songs_serializers


class SongModelViewSet(ModelViewSet):
    model = songs_models.Song
    serializer_class = songs_serializers.SongModelSerializer
    queryset = songs_models.Song.objects.all()
    pagination_class = None
