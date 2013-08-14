# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserModels

admin.site.unregister(User)

class CustomUserAdmin(admin.ModelAdmin):
    class Meta:
        model = UserModels


admin.site.register(UserModels, CustomUserAdmin)