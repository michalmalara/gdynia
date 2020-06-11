from django.contrib import admin

from .models import Attraction
from user.models import User


# Register your models here.

class AttractionAdminView(admin.ModelAdmin):
    list_display = ['name', 'id', 'location', 'description']
    search_fields = ['name', 'location']
    readonly_fields = []

    filter_horizontal = ()
    list_filter = ('location',)
    fieldsets = ()


admin.site.register(Attraction, AttractionAdminView)
