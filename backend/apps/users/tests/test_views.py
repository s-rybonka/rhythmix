from django.urls import reverse
from rest_framework import status


class TestUserViewSet:

    def test_user_profile_fetch(self, api_client, user):
        api_url = reverse('user-profile')
        response = api_client.get(api_url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        api_client.force_authenticate(user)
        response = api_client.get(api_url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == user.id
        assert response.data['email'] == user.email
        assert response.data['full_name'] == user.full_name
        assert response.data['short_name'] == user.short_name
        assert response.data['description'] == user.description
        assert response.data['job_title'] == user.job_title
        assert response.data['skills'] == user.skills
        assert response.data['phone_number'] == user.phone_number
        assert response.data['location'] == user.location
        assert response.data['short_description'] == user.short_description

    def test_user_login_ok(self, api_client, user):
        api_url = reverse('user-login')

        response = api_client.post(api_url, data={
            'email': user.email,
            'password': '12345Qwerty',
        })
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == user.id
        assert response.data['email'] == user.email
        assert response.data['full_name'] == user.full_name
        assert response.data['short_name'] == user.short_name

    def test_user_login_fail(self, api_client, user):
        api_url = reverse('user-login')

        response = api_client.post(api_url, data={
            'email': user.email,
            'password': 'WrongPass',
        })
        assert response.status_code == status.HTTP_404_NOT_FOUND
