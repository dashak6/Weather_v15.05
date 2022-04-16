from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_page, name="auth-page"),
    path('logout', views.logout_view, name='logout'),
    path('main', views.main, name='main-page'),
    path('meteo-data', views.meteo_data, name='meteo-data'),
    path('wind-data', views.wind_data, name='wind-data'),
    path('download/meteo-data', views.download_meteo_data, name='download-meteo-data'),
    path('download/wind-data', views.download_wind_data, name='download-wind-data')
]
