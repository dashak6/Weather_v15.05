from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_page, name="auth-page"),
    path('reg', views.reg_view, name="reg-page"),
    path('logout', views.logout_view, name='logout'),
    path('main', views.main, name='main-page'),
    path('meteo-data', views.meteo_data, name='meteo-data'),
    path('meteo-data/<int:pk>', views.meteo_data_pk, name='meteo-data-pk'),
    path('wind-data', views.wind_data, name='wind-data'),
    path('invertor-data', views.invertor_data, name='invertor-data'),
    path('download/meteo-data', views.download_meteo_data, name='download-meteo-data'),
    path('download/meteo-data-xlsx', views.download_meteo_data_xlsx, name='download-meteo-data-xlsx'),
    path('download/wind-data', views.download_wind_data, name='download-wind-data'),
    path('download/wind-data-xlsx', views.download_wind_data_xlsx, name='download-wind-data-xlsx'),
    path('download/invertor-data', views.download_invertor_data, name='download-invertor-data'),
    path('download/invertor-data-xlsx', views.download_invertor_data_xlsx, name='download-invertor-data-xlsx'),
    path('meteo-data/graph', views.create_meteo_graph, name='meteo-data-graph'),
]
