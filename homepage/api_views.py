# import models
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

from .models import Attraction
from user.models import User

# import serializers
from .serializers import (
    AttractionSerializer,
    AttractionDetailSerializer,
    UsersSerializer,
    RegisterUserSerializer,
    LikeUnlikeSerializer)

from rest_framework import viewsets, status, permissions, authentication
from rest_framework.views import Response


# Attraction API viewsets:
class AttractionsAPIView(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AttractionDetailAPIView(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LikeUnlikeAPIView(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = LikeUnlikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def update(self, request, pk=None):
        user = request.user
        # print(pk)
        attraction = Attraction.objects.get(pk=pk)
        if attraction.users_liked.filter(pk=user.pk).exists():
            attraction.users_liked.remove(user)
            return Response({'action': 'unliked'}, status=status.HTTP_200_OK)
        else:
            attraction.users_liked.add(user)
            return Response({'action': 'liked'}, status=status.HTTP_200_OK)
        attraction.save()

        return Response({'data': 'ok'})

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)


# User API viewsets
class UsersAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


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


