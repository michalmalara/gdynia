from django.contrib import admin

from .models import Attraction
from user.models import User

# Register your models here.

class AttractionAdminVirew(admin.ModelAdmin):
    list_display = ['name', 'location', 'description']
    search_fields = ['name', 'location']
    readonly_fields = []

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Attraction, AttractionAdminVirew)
