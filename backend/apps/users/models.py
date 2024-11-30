from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from users import managers as users_managers


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', unique=True, max_length=255)
    first_name = models.CharField(verbose_name='First name', max_length=30, default='first')
    last_name = models.CharField(verbose_name='Last name', max_length=30, default='last')
    avatar = models.ImageField(verbose_name='Avatar', blank=True)
    token = models.UUIDField(verbose_name='Token', default=uuid4, editable=False)
    is_admin = models.BooleanField(verbose_name='Admin', default=False)
    is_active = models.BooleanField(verbose_name='Active', default=True)
    is_staff = models.BooleanField(verbose_name='Staff', default=False)
    registered_at = models.DateTimeField(verbose_name='Registered at', auto_now_add=timezone.now)

    # Fields settings
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = users_managers.UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def short_name(self):
        return f'{self.last_name} {self.first_name[0]}.'

    def __str__(self):
        return self.full_name
