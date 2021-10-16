from django.contrib import admin
from django.urls import path
from api import views
from api.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('songlcapi/', views.LCSongAPI.as_view()),
    path('podcastlcapi/', views.LCPodcastAPI.as_view()),
    path('audiobooklcapi/', views.LCAudioBookAPI.as_view()),

    path('songrudapi/<int:pk>', views.RUDSongAPI.as_view()),
    path('audiobookrudapi/<int:pk>', views.RUDAudioBookAPI.as_view()),
    path('podcastrudapi/<int:pk>', views.RUDPodcastAPI.as_view()),
    
]
