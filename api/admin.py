from django.contrib import admin
from .models import Song, Participants, Podcast, AudioBook

# Register your models here.

@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(AudioBook)
class AudioBookAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'duration']

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'duration']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'duration']