# Generated by Django 3.0.6 on 2020-06-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200605_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='Gdynia_herb.png', upload_to='', verbose_name='Awatar'),
        ),
    ]
