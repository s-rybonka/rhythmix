from django.db import models as dj_models
from django.utils.translation import gettext_lazy as _


class Song(dj_models.Model):
    title = dj_models.CharField(verbose_name=_('title'), max_length=150)
    author = dj_models.CharField(verbose_name=_('author'), max_length=100)
    summary = dj_models.TextField(verbose_name=_('summary'), max_length=500, blank=True)
    countries = dj_models.CharField(verbose_name=_('countries'), max_length=200, blank=True)
    created_at = dj_models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_at = dj_models.DateTimeField(verbose_name=_('updated at'), auto_now=True)

    class Meta:
        verbose_name = _('Song')
        verbose_name_plural = _('Songs')
        ordering = ('-id',)

    def __str__(self):
        return self.title
