from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from apps.users.forms import UserChangeForm
from apps.users.forms import UserCreationForm
from apps.users.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['full_name', 'email']
    fieldsets = [
        ['Auth', {'fields': ['email', 'password']}],
        ['Personal info', {
            'fields': [
                'last_name', 'first_name', 'avatar', 'phone_number', 'description',
                'short_description', 'job_title', 'skills', 'location'
            ]
        }
         ],
        ['Settings', {'fields': ['groups', 'is_admin', 'is_active', 'is_staff', 'is_superuser']}],
        ['Important dates', {'fields': ['last_login', 'registered_at']}],
    ]
    add_fieldsets = [
        [None, {
            'classes': ['wide'],
            'fields': ['email', 'first_name', 'last_name', 'password1', 'password2']
        }],
    ]
    search_fields = ['email']
    ordering = ['email']
    readonly_fields = ['last_login', 'registered_at']


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
