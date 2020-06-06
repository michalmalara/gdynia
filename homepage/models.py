from django.db import models

from user.models import User
# Create your models here.

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    users_liked = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f'{self.name}'
