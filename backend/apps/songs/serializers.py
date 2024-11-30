from django.core.exceptions import ValidationError as DJValidationError
from rest_framework import serializers as drf_serializers

from songs import models as songs_models
from songs import services as songs_services


class SongModelSerializer(drf_serializers.ModelSerializer):
    api_service = songs_services.OpenAIAPIService()

    class Meta:
        model = songs_models.Song
        fields = ('id', 'title', 'author', 'summary', 'countries')

    def create(self, validated_data):
        title = validated_data.get('title')
        author = validated_data.get('author')

        try:
            summary, countries = self.api_service.generate_summary(title, author)
            validated_data.update(
                summary=f'{summary}.'.strip(),
                countries=f'{countries}.'.strip(),
            )

        except DJValidationError as e:
            raise drf_serializers.ValidationError(e)

        return super().create(validated_data)
