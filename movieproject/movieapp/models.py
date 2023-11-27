from django.db import models


class UserDetails(models.Model):
    fullname = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 8)
    con_password = models.CharField(max_length = 8)

class AddMovies(models.Model):
    movieName = models.CharField(max_length = 100)
    movieYear = models.IntegerField(null = True)
    movieSummary = models.TextField(max_length = 300)
    poster = models.ImageField(upload_to ='images/',null = True)
    banner = models.ImageField(upload_to = 'images/',null = True)
    rating = models.IntegerField(null = True)
    language = models.CharField(max_length = 50,default = 'LANGUAGE')
    joner1 = models.CharField(max_length = 50,default = 'A')
    joner2 = models.CharField(max_length = 50,default = 'B')
    joner3 = models.CharField(max_length = 50,default =  'C')
    censor = models.CharField(max_length = 25,default = 'D')
    duration = models.CharField(max_length = 10, default = 'Duration')
    releasingDate = models.CharField(max_length = 20,default = 'Date')
    movieFromat = models.CharField(max_length = 20,default='Format')
    actor_img1 = models.ImageField(upload_to = 'images/',null = True)
    actor_Name1 = models.CharField(max_length = 50,default = 'Name')
    actor_img2 = models.ImageField(upload_to = 'images/',null = True)
    actor_Name2 = models.CharField(max_length = 50,default = 'Name')
    actor_img3 = models.ImageField(upload_to = 'images/',null = True)
    actor_Name3 = models.CharField(max_length = 50,default = 'Name')
    actor_img4 = models.ImageField(upload_to = 'images/',null = True)
    actor_Name4 = models.CharField(max_length = 50,default = 'Name')

