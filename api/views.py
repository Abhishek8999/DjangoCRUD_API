import rest_framework
from .models import AudioBook, Song, Participants, Podcast
from .serializers import ParticipantSerializer, SongSerializer, PodcastSerializer, AudioBookSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


'''
================
LIST AND CREATE 
================
'''
# GET DATA
class LCSongAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    # Lists all Songs from the database
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Create new songs data and lists all Songs from the database
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LCPodcastAPI(GenericAPIView,ListModelMixin, CreateModelMixin):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LCAudioBookAPI(GenericAPIView,ListModelMixin, CreateModelMixin):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




'''
=========================
RETRIVE UPDATE AND DELETE 
=========================
'''
# AudioBook RETRIEVE UPDATE DELETE

class RUDSongAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Podcast RETRIEVE UPDATE DELETE

class RUDPodcastAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# AudioBook RETRIEVE UPDATE DELETE

class RUDAudioBookAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
