from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    video_url = models.URLField()
    image = models.ImageField(upload_to='movie/image/')
    time = models.DateTimeField(auto_now_add=True)
    see = models.IntegerField(default=0)
    
class ViewUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie2 = models.ForeignKey(movie, on_delete=models.CASCADE)
    rate = models.PositiveBigIntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])

class site_about(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
class live_chanel(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    video_url = models.URLField()
    image = models.ImageField(upload_to='movie/image/')
    time = models.DateTimeField(auto_now_add=True)
    see = models.IntegerField(default=0)

class channelviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    livechannel = models.ForeignKey(live_chanel, on_delete=models.CASCADE)


