from django.contrib import admin
from meteo_app.models import MeteoData, WindData

admin.site.register(MeteoData)
admin.site.register(WindData)
