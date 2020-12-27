

# Create your models here.
from django.db import models
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=32)


class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title



class Hotel(models.Model):
    Bio = models.TextField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='profile_pic/')

