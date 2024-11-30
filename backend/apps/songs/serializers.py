from rest_framework import serializers as drf_serializers

from songs import models as songs_models


class SongModelSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = songs_models.Song
        fields = ('id', 'title', 'author', 'summary')
