from django.utils.translation import gettext_lazy as _
from rest_framework import serializers as drf_serializers

from songs import exceptions as songs_exceptions
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
                summary=f'{summary}'.strip(),
                countries=f'{countries}'.strip(),
            )
        except songs_exceptions.OpenAIAPIException as e:
            raise drf_serializers.ValidationError({'message': e})

        except ValueError:
            raise drf_serializers.ValidationError({
                'message': _("Invalid form data, author, and/or title are not real. "
                             "Please fix it and try again.")
            })

        return super().create(validated_data)
