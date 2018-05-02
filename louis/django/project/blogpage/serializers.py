from rest_framework import serializers

from .models import Anime, Breed, Website

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ('title','description','director','release_date','score','picture')

class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'
