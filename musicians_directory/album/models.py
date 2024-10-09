from django.db import models
from musician . models import Musician
from django.contrib.auth.models import User
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_date = models.DateField(auto_now=True)
    RATING_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    album_rating = models.IntegerField(choices=RATING_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Link to User

    def __str__(self):
        return self.album_name
