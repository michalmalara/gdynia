from django.db import models


# Create your models here.

class Attraction(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.name}'
