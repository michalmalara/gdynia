# import models
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

from .models import Attraction
from user.models import User

# import serializers
from .serializers import AttractionSerializer, AttractionDetailSerializer, UsersSerializer, RegisterUserSerializer

from rest_framework import viewsets, status, permissions
from rest_framework.views import Response


class AttractionsAPIView(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AttractionDetailAPIView(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionDetailSerializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UsersAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class RegisterNewUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = []

    def create(self, request):
        if request.method == 'POST':
            serializer = RegisterUserSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                user = serializer.save()
                data['response'] = 'Utworzono konto użytkownika'
                data['username'] = user.username
                data['email'] = user.email
                data['token'] = Token.objects.get(user=user).key
            else:
                data = serializer.errors
            return Response(data, status=status.HTTP_201_CREATED)
