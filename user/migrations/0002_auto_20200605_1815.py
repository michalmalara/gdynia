# Generated by Django 3.0.6 on 2020-06-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=60, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=10, unique=True, verbose_name='Nazwa użytkownika'),
        ),
    ]
