from django.urls import reverse
from rest_framework import status

from songs.tests import factories


class TestSongModelViewSet:

    def test_items_list_fetch(self, api_client, user):
        factories.SongFactory.create_batch(10)

        api_url = reverse('song-list')

        response = api_client.get(api_url)

        assert response.status_code == status.HTTP_403_FORBIDDEN

        api_client.force_authenticate(user)

        response = api_client.get(api_url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10

    def test_items_detail_fetch(self, api_client, user):
        song = factories.SongFactory()

        api_url = reverse('song-detail', args=(song.id,))

        response = api_client.get(api_url)

        assert response.status_code == status.HTTP_403_FORBIDDEN

        api_client.force_authenticate(user)

        response = api_client.get(api_url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == song.id
        assert response.data['title'] == song.title
        assert response.data['author'] == song.author
        assert response.data['summary'] == song.summary
        assert response.data['countries'] == song.countries
