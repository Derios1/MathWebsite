from django.contrib import admin
from user_profile.models import Profile


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ["user", "bio", "rating"]

