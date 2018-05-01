from django.contrib import admin

from .models import Anime, Breed, Website

# Register your models here.

admin.site.register(Anime)
admin.site.register(Breed)
admin.site.register(Website)
