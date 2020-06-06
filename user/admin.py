from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from.models import User


# Register your models here.

class UserAdminView(UserAdmin):
    list_display = ['username', 'email', 'date_joined', 'last_login', 'is_admin', 'is_staff']
    search_fields = ['username', 'email']
    readonly_fields = ['date_joined', 'last_login',]

    filter_horizontal = ()
    list_filter = ('is_admin', 'is_staff')
    fieldsets = ()


admin.site.register(User, UserAdminView)
