# Generated by Django 3.0.6 on 2020-06-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]