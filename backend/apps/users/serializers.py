from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    registered_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y', read_only=True)
    avatar = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)
    short_name = serializers.SerializerMethodField(read_only=True)
    skills_list = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_avatar(obj):
        return obj.avatar.url if obj.avatar else settings.STATIC_URL + 'images/default_avatar.png'

    @staticmethod
    def get_full_name(obj):
        return obj.full_name

    @staticmethod
    def get_short_name(obj):
        return obj.short_name

    @staticmethod
    def get_skills_list(obj):
        return obj.skills_list

    @staticmethod
    def get_token(obj):
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key

    class Meta:
        model = User
        fields = [
            'id', 'email', 'avatar', 'full_name', 'short_name', 'registered_at', 'token',
            'description', 'job_title', 'skills', 'phone_number',
        ]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(label='Email')
    password = serializers.CharField(min_length=8)
