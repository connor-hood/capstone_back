from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    playlist = models.ForeignKey('Playlist',
                                 on_delete=models.CASCADE,
                                 related_query_name='Playlist.user')
    favorite = models.ForeignKey('Favorite', on_delete=models.CASCADE)


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=50)
    playlist_description = models.CharField(max_length=200)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_query_name='User.playlist')
    song = models.ForeignKey('Song',
                             on_delete=models.CASCADE,
                             related_query_name='Song.Playlist')


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=100)
    ranking = models.IntegerField()
    artwork = models.URLField()
    playlist = models.ManyToManyField(Playlist,
                                      related_query_name='Playlist.song')


class Favorite(models.Model):
    name = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_query_name='User.favorite')
    song = models.ManyToManyField(Song)
