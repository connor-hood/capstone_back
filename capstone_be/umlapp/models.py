from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=100)
    ranking = models.IntegerField()
    artwork = models.URLField()


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=50)
    playlist_description = models.CharField(max_length=200)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_query_name='User.playlist',
                             blank=True)
    song = models.ManyToManyField(Song,
                                  related_query_name='Song.playlist',
                                  null=True)


class Favorite(models.Model):
    name = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_query_name='User.favorite',
                             blank=True)
    song = models.ManyToManyField(Song,
                                  null=True)
