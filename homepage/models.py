from django.db import models

from user.models import User
# Create your models here.


class Attraction(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa atrakcji')
    image = models.ImageField(upload_to='attractions/', verbose_name='Zdjęcie')
    location = models.CharField(max_length=50, verbose_name='Lokalizacja')
    description = models.TextField(max_length=10000, verbose_name='Opis')

    users_liked = models.ManyToManyField(User, blank=True, verbose_name='Osoby, które polubiły')

    def __str__(self):
        return f'{self.name}'
