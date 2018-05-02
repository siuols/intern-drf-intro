from django.shortcuts import get_object_or_404

from django.shortcuts import render

from rest_framework import viewsets, status, permissions

from rest_framework.response import Response

from .models import Breed, Anime, Website

from .serializers import  AnimeSerializer, BreedSerializer, WebsiteSerializer

# Create your views here.

class AnimeViewSet(viewsets.ViewSet):
    # permission_classes = [permissions.AllowAny, ]
    def list(self, request):
        queryset = Anime.objects.all()
        serializer = AnimeSerializer(queryset, many=True)
        return Response(serializer.data)

class BreedModelViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [permissions.AllowAny, ]

class WebsiteModelViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = [permissions.AllowAny, ]
