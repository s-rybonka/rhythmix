from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import LoginSerializer
from apps.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    serializer_classes = {
        'list': UserSerializer,
        'login': LoginSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action) or super().get_serializer_class()

    @action(methods=['GET'], detail=False)
    def profile(self, request):
        if request.user.is_authenticated:
            serializer = self.serializer_class(request.user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def login(self, request):
        serializer = self.get_serializer(request, request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        email = validated_data.get('email', None)
        password = validated_data.get('password', None)
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK, data=UserSerializer(user).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['POST'], detail=False)
    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
