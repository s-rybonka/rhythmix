from django.contrib import admin

from songs import models as songs_models


@admin.register(songs_models.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'summary', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'summary')
