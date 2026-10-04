# admin.py
from django.contrib import admin
from .models import BirthdayWish

@admin.register(BirthdayWish)
class BirthdayWishAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'text')