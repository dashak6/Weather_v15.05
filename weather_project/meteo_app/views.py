import os
from weather_project.settings import BASE_DIR
from meteo_app.models import MeteoData, WindData
from meteo_app.forms import AuthForm
from meteo_app.services import model_data_to_csv
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def auth_page(request):
    message = None
    if request.user.is_authenticated:
        return redirect('main-page')
    
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main-page')
            else:
                message = "Неправильный логин или пароль"
    else:
        form = AuthForm()
    
    context = {
        'form': form,
        'message': message
    }    
    return render(request, 'meteo_app/auth.html', context)


def main(request):
    if request.user.is_authenticated:
        context = {'user': request.user}
        return render(request, 'meteo_app/main.html', context)
    return redirect('auth-page')


def logout_view(request):
    logout(request)
    return redirect('auth-page')


def meteo_data(request):
    if request.user.is_authenticated:
        data = MeteoData.objects.get(id=1)
        context = {
            'data': data,
            'user': request.user
        }
        return render(request, 'meteo_app/meteo.html', context)
    return redirect('auth-page')


def wind_data(request):
    if request.user.is_authenticated:
        data = WindData.objects.get(id=1)
        context = {
            'data': data,
            'user': request.user
        }
        return render(request, 'meteo_app/wind.html', context)
    else:
        return redirect('auth-page')


def download_meteo_data(request):
    filepath = os.path.join(str(BASE_DIR)+"/meteo_app/files/meteo.csv")
    model_data_to_csv(MeteoData, filepath)
    to_download = open(filepath, 'rb')
    response = FileResponse(to_download, content_type="application/force-download")
    response['Content-Disposition'] = 'attachment; filename="meteodata.csv"'
    return response


def download_wind_data(request):
    filepath = os.path.join(str(BASE_DIR)+"/meteo_app/files/wind.csv")
    model_data_to_csv(WindData, filepath)
    to_download = open(filepath, 'rb')
    response = FileResponse(to_download, content_type="application/force-download")
    response['Content-Disposition'] = 'attachment; filename="winddata.csv"'
    return response
