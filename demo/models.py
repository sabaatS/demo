from django.db import models

# Create your models here.



class Album(models.Model):
    album_name =models.CharField(max_length=100)
    singer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.album_name}--{self.singer}"


class Song(models.Model):
    album_name = models.ForeignKey(Album, on_delete = models.CASCADE)
    song_name = models.CharField(max_length=100)    

    def __str__(self):
        return f"{self.album_name}--{self.song_name}"
