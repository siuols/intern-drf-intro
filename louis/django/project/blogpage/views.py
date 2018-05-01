from django.shortcuts import render

from rest_framework import viewsets, status, permissions

from .models import Breed, Anime, Website

from .serializers import  AnimeSerializer, BreedSerializer, WebsiteSerializer

# Create your views here.

class AnimeModelViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [permissions.AllowAny, ]

class BreedModelViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [permissions.AllowAny, ]

class WebsiteModelViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = [permissions.AllowAny, ]
