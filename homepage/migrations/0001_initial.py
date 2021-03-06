# Generated by Django 3.0.6 on 2020-06-05 10:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('location', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('users_liked', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
