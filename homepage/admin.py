from django.contrib import admin
from .models import Attraction
from user.models import User

# Register your models here.
admin.site.register(Attraction)
admin.site.register(User)
