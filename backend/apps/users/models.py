from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users import managers as users_managers


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('Email'), unique=True, max_length=255)
    first_name = models.CharField(verbose_name=_('First name'), max_length=30, default='first')
    last_name = models.CharField(verbose_name=_('Last name'), max_length=30, default='last')
    avatar = models.ImageField(verbose_name=_('Avatar'), blank=True, upload_to='avatars/')
    is_admin = models.BooleanField(verbose_name=_('Admin'), default=False)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    is_staff = models.BooleanField(verbose_name=_('Staff'), default=False)
    registered_at = models.DateTimeField(verbose_name=_('Registered at'), auto_now_add=timezone.now)
    description = models.TextField(verbose_name=_('Description'), max_length=500, blank=True)
    job_title = models.CharField(verbose_name=_('Job Title'), max_length=100, blank=True)
    skills = models.CharField(verbose_name=_('Skills'), max_length=250, blank=True)
    phone_number = models.CharField(verbose_name=_('Phone number'), max_length=20, blank=True)


    # Fields settings
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = users_managers.UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def short_name(self):
        return f'{self.last_name} {self.first_name[0]}.'
