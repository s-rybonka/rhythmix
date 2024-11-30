from django.urls import path
from drf_spectacular import views as drf_spec_views
from rest_framework import routers

from apps.users.views import UserViewSet
from songs.views import SongModelViewSet


# Settings
api_router = routers.DefaultRouter()
api_router.trailing_slash = '/?'

# APIs
api_router.register('users', UserViewSet)
api_router.register('songs', SongModelViewSet)

urlpatterns = [
    path('schema/', drf_spec_views.SpectacularAPIView.as_view(), name='schema'),
    path('docs/', drf_spec_views.SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    *api_router.urls
]
