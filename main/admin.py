from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from . import models

# Register your models here.
@admin.register(models.CustomMaps)
class CustomMapsAdmin(admin.ModelAdmin):
    list_display = ['title', 'center', 'tiles_in_folders']
    search_fields = ['title']


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'custom_map']
    search_fields = ['title', 'custom_map']

@admin.register(models.Pins)
class PinsAdmin(admin.ModelAdmin):
    list_display = ['title', 'pin_type', 'category', 'icon']
    search_fields = ['title', 'pin_type']

@admin.register(models.Icons)
class IconsAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_type']
    search_fields = ['title', 'icon_type']


@admin.register(models.PinCategory)
class PinCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'project']
    search_fields = ['title', 'icon', 'project']

@admin.register(models.PinSubCategory)
class PinSubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    search_fields = ['title', 'category']

AdminSite.site_title = "Map Maker"
AdminSite.site_header = "Map Maker"