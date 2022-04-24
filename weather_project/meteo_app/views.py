import os
from weather_project.settings import BASE_DIR
from meteo_app.models import MeteoData, WindData
from meteo_app.services import model_data_to_csv, model_data_to_xls
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def auth_page(request):
    message = None
    if request.user.is_authenticated:
        return redirect('main-page')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main-page')
        else:
            message = "Неправильный логин или пароль"
    
    context = {
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
        dataset = None
        if "date_from" in request.GET and "date_to" in request.GET:
            if request.GET["date_from"] and request.GET["date_from"]:
                start = request.GET["date_from"]
                end = request.GET["date_to"]
                dataset = MeteoData.objects.filter(date__range=(start, end))
        if not dataset:
            dataset = MeteoData.objects.order_by('id')
            dataset = dataset.reverse()[:10]
        context = {
            'dataset': dataset,
            'user': request.user
        }
        return render(request, 'meteo_app/meteo.html', context)
    else:
        dataset = MeteoData.objects.order_by('id')
        dataset = dataset.reverse()[:10]
        context = {
            'dataset': dataset,
            'user': request.user
        }
        return render(request, 'meteo_app/meteo.html', context)


def meteo_data_pk(request, pk):
    if request.user.is_authenticated:
        data = MeteoData.objects.get(id=pk)
        context = {
            'data': data,
            'user': request.user
        }
        return render(request, 'meteo_app/meteo.html', context)
    return redirect('auth-page')


def wind_data(request):
    if request.user.is_authenticated:
        dataset = None
        if "date_from" in request.GET and "date_to" in request.GET:
            if request.GET["date_from"] and request.GET["date_from"]:
                start = request.GET["date_from"]
                end = request.GET["date_to"]
                dataset = WindData.objects.filter(date__range=(start, end))
        if not dataset:
            dataset = WindData.objects.order_by('id')
            dataset = dataset.reverse()[:10]
        context = {
            'dataset': dataset,
            'user': request.user
        }
        return render(request, 'meteo_app/wind.html', context)
    else:
        dataset = WindData.objects.order_by('id')
        dataset = dataset.reverse()[:10]
        context = {
            'dataset': dataset,
            'user': request.user
        }
        return render(request, 'meteo_app/wind.html', context)


def download_meteo_data(request):
    if request.user.is_authenticated:
        filepath = os.path.join(str(BASE_DIR)+"/meteo_app/files/meteo.csv")
        model_data_to_csv(MeteoData, filepath)
        to_download = open(filepath, 'rb')
        response = FileResponse(to_download, content_type="application/force-download")
        response['Content-Disposition'] = 'attachment; filename="meteodata.csv"'
        return response
    return redirect('auth-page')


def download_meteo_data_xlsx(request):
    if request.user.is_authenticated:
        filepath = os.path.join(str(BASE_DIR)+"/meteo_app/files/meteo.xlsx")
        model_data_to_xls(MeteoData, filepath)
        to_download = open(filepath, 'rb')
        response = FileResponse(to_download, content_type="application/force-download")
        response['Content-Disposition'] = 'attachment; filename="meteodata.xlsx"'
        return response
    return redirect('auth-page')


def download_wind_data(request):
    if request.user.is_authenticated:
        filepath = os.path.join(str(BASE_DIR)+"/meteo_app/files/wind.csv")
        model_data_to_csv(WindData, filepath)
        to_download = open(filepath, 'rb')
        response = FileResponse(to_download, content_type="application/force-download")
        response['Content-Disposition'] = 'attachment; filename="winddata.csv"'
        return response
    return redirect('auth-page')


def download_wind_data_xlsx(request):
    if request.user.is_authenticated:
        filepath = os.path.join(str(BASE_DIR)+"/meteo_app/files/wind.xlsx")
        model_data_to_xls(WindData, filepath)
        to_download = open(filepath, 'rb')
        response = FileResponse(to_download, content_type="application/force-download")
        response['Content-Disposition'] = 'attachment; filename="winddata.xlsx"'
        print(dir(response))
        return response
    return redirect('auth-page')
