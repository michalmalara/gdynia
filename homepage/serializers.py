# import models
from .models import Attraction

# import REST framework necessary modules
from rest_framework import serializers


# serializer for Attractions model
class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = '__all__'
