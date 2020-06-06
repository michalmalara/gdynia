# import models
from .models import Attraction
from user.models import User

# import REST framework necessary modules
from rest_framework import serializers


# serializer for Attractions model
class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attraction
        fields = ['id', 'url', 'name', 'location', 'image']


class AttractionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = '__all__'


# serializer for user
class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'date_joined', 'last_login']


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Hasła muszą być takie same.'})
        else:
            user.set_password(password)
            user.save()
        return user
