from django.db import models

# Create your models here.

from django.db import models

# Model for participants it represents the table in relational database
class Participants(models.Model):
    name = models.CharField(max_length = 150, null=False, blank = False)

    def __str__(self):
        return self.name


# Model for Song it represents the table in relational database
class Song(models.Model):
    name = models.CharField(max_length = 150, null=False, blank = False)
    duration = models.IntegerField(null=False, blank = False)
    uploaded = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


# Model for Podcast it represents the table in relational database
class Podcast(models.Model):
    name = models.CharField(max_length = 150, null=False, blank = False)
    duration = models.IntegerField(null=False, blank = False)
    uploaded = models.DateTimeField(auto_now_add = True)
    host = models.ForeignKey('api.Participants', on_delete=models.SET_NULL,null=True, related_name ="host")
    participants = models.ManyToManyField('api.Participants', related_name = "participants")

    def __str__(self):
        return self.name


# Model for AudioBook it represents the table in relational database
class AudioBook(models.Model):
    name = models.CharField(max_length = 150, null=False, blank = False)
    duration = models.IntegerField(null=False, blank = False)
    uploaded = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey('api.Participants', on_delete=models.SET_NULL,null=True, related_name="author")
    narrator = models.ForeignKey('api.Participants', on_delete=models.SET_NULL,null=True, related_name="narrator")

    def __str__(self):
        return self.name
