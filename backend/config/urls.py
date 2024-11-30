from config.api import urlpatterns as api_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include(api_urlpatterns)),
]
