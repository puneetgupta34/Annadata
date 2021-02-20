from django.db import models

# Create your models here.

class Crop(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    duration = models.CharField(max_length=100)

class Front(models.Model):
    logo = models.ImageField(upload_to = 'pics')
    slider1 = models.ImageField(upload_to = 'pics')
    slider2 = models.ImageField(upload_to = 'pics')
    slider3 = models.ImageField(upload_to = 'pics')
    slider4 = models.ImageField(upload_to = 'pics')
    
    


class Seed(models.Model):
    name = models.CharField(max_length=100)
    
