from django.contrib import admin

# Register your models here.
from black_clover.grimorios.models import Grimorio, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "social_status", "status"]
    pass


@admin.register(Grimorio)
class GrimorioAdmin(admin.ModelAdmin):
    list_display = ["profile", "get_cover_display"]
