from django.contrib import admin
from meteo_app.models import MeteoData, WindData
from django.contrib.admin import AdminSite

@admin.register(MeteoData)
class MeteoDataAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    
@admin.register(WindData)
class WindDataAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
