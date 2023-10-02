# musicians/admin.py
from django.contrib import admin
from .models import Musician, MusicianPortrait

admin.site.register(Musician)
admin.site.register(MusicianPortrait)
