from django.db import models


class UserDetails(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    con_password = models.CharField(max_length=8)


class AddMovies(models.Model):
    movieName = models.CharField(max_length=100)
    movieYear = models.IntegerField(null=True)
    movieSummary = models.TextField(max_length=300)
    poster = models.ImageField(upload_to='images/',null=True)


