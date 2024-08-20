from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
# Register your models here.


class CustomModelAdmin(UserAdmin):
    model=settings.AUTH_USER_MODEL
    list_display = ['username','name']
admin.site.register(User,CustomModelAdmin)
