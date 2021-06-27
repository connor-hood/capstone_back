from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=50)
    playlist_description = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=100)
    ranking = models.IntegerField()
    artwork = models.URLField()
    playlist = models.ManyToManyField(Playlist)


class Favorites(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
