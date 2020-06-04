# import models
from .models import Attraction

# import serializers
from .serializers import AttractionSerializer, AttractionDetailSerializer

from rest_framework import viewsets, status
from rest_framework.views import Response

class AttractionsAPIView(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


class AttractionDetailAPIView(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionDetailSerializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)
