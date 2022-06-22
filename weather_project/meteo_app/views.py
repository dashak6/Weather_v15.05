
# студентки группы А-12-18
# Красавиной Дарьи Дмитриевны

# Листинг модуля "views.py" приложения "myapp", класса "ProjectData"

# ==========

# Импортируемые модули
import os
from weather_project.settings import BASE_DIR
from meteo_app.models import MeteoData, WindData, Invertor
from meteo_app.services import model_data_to_csv, model_data_to_xls, get_page_obj
from meteo_app.graph import plot_graphic
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

    
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


def reg_view(request):
    message = None
    
    if request.user.is_authenticated:
        return redirect('main-page')
    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            password2 = request.POST["password2"]
            if password == password2:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return render(request, 'meteo_app/auth.html', {'message': 'Регистрация успешна'})
            else:
                message = "Пароли не совпадают"
    
    context = {
        'message': message
    }

    return render(request, 'meteo_app/reg.html', context)
            
    
def main(request):
    if request.user.is_authenticated:
        context = {'user': request.user}
        return render(request, 'meteo_app/main.html', context)
    return redirect('main-logout')


def main_logout(request):
    return render(request, 'meteo_app/main.html')


def logout_view(request):
    logout(request)
    return redirect('main-page')


def info_view(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "meteo_app/info.html")


def meteo_data(request):
    if request.user.is_authenticated:
        dataset = None
        message = None
        if "date_from" in request.GET and "date_to" in request.GET:
            try:
                if request.GET["date_from"] and request.GET["date_from"]:
                    start = request.GET["date_from"]
                    end = request.GET["date_to"]
                    dataset = MeteoData.objects.filter(date__range=(start, end))
                    dataset = get_page_obj(
                        request=request, model=None, size=100, queryset=dataset)
                    
            except ValidationError:
                message = "Данные введены неправильно"
                redirect('meteo-data')
                
        if not dataset:
            dataset = MeteoData.objects.order_by('id')
            dataset = get_page_obj(
                request=request, model=MeteoData, size=10, queryset=dataset)
        
        context = {
            'page_obj': dataset,
            'user': request.user,
            'message': message
        }
        return render(request, 'meteo_app/meteo.html', context)
    else:
        dataset = MeteoData.objects.order_by('id')
        dataset = get_page_obj(
            request=request, model=MeteoData, size=10, queryset=dataset)
        context = {
            'page_obj': dataset,
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
        message = None
        try:
            if "date_from" in request.GET and "date_to" in request.GET:
                if request.GET["date_from"] and request.GET["date_from"]:
                    start = request.GET["date_from"]
                    end = request.GET["date_to"]
                    dataset = WindData.objects.filter(date__range=(start, end))
                    dataset = get_page_obj(
                        request=request, model=None, size=100, queryset=dataset)

        except ValidationError:
                message = "Данные введены неправильно"
                redirect('wind-data')
        
        if not dataset:
            dataset = WindData.objects.order_by('id')
            dataset = get_page_obj(request=request, model=WindData, size=10, queryset=dataset)

        context = {
            'page_obj': dataset,
            'user': request.user,
            'message': message,
        }
        return render(request, 'meteo_app/wind.html', context)
    else:
        dataset = WindData.objects.order_by('id')
        dataset = get_page_obj(request=request, model=WindData, size=10, queryset=dataset)
        context = {
            'page_obj': dataset,
            'user': request.user
        }
        return render(request, 'meteo_app/wind.html', context)


def invertor_data(request):
    if request.user.is_authenticated:
        dataset = None
        message = None
        if "date_from" in request.GET and "date_to" in request.GET:
            try:
                if request.GET["date_from"] and request.GET["date_from"]:
                    start = request.GET["date_from"]
                    end = request.GET["date_to"]
                    dataset = Invertor.objects.filter(date__range=(start, end))
                    dataset = get_page_obj(
                        request=request, model=None, size=100, queryset=dataset)

            except ValidationError:
                message = "Данные введены неправильно"
                redirect('invertor-data')

        if not dataset:
            dataset = Invertor.objects.order_by('id')
            dataset = get_page_obj(request=request, model=Invertor, size=10, queryset=dataset)

        context = {
            'page_obj': dataset,
            'user': request.user,
            'message': message
        }
        return render(request, 'meteo_app/invertor.html', context)
    else:
        dataset = Invertor.objects.order_by('id')
        dataset = get_page_obj(request=request, model=Invertor, size=10, queryset=dataset)

        context = {
            'page_obj': dataset,
            'user': request.user
        }
        return render(request, 'meteo_app/invertor.html', context)


##### DOWNLOADING VIEWS
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


def download_invertor_data(request):
    if request.user.is_authenticated:
        filepath = os.path.join(str(BASE_DIR)+"/meteo_app/files/invertor.csv")
        model_data_to_csv(WindData, filepath)
        to_download = open(filepath, 'rb')
        response = FileResponse(to_download, content_type="application/force-download")
        response['Content-Disposition'] = 'attachment; filename="invertordata.csv"'
        return response
    return redirect('auth-page')


def download_invertor_data_xlsx(request):
    if request.user.is_authenticated:
        filepath = os.path.join(str(BASE_DIR)+"/meteo_app/files/invertor.xlsx")
        model_data_to_xls(WindData, filepath)
        to_download = open(filepath, 'rb')
        response = FileResponse(to_download, content_type="application/force-download")
        response['Content-Disposition'] = 'attachment; filename="invertordata.xlsx"'
        return response
    return redirect('auth-page')


# GRAPH VIEWS
def create_meteo_graph(request):
    if request.user.is_authenticated:
        dataset = None
        gr = False
        message = None
        if "date_from" in request.GET and "date_to" in request.GET:
            try:
                if request.GET["date_from"] and request.GET["date_from"] and request.GET["param"]:
                    start = request.GET["date_from"]
                    end = request.GET["date_to"]
                    param = request.GET["param"]
                    #TODO: сделать для wind и invertor
                    seconds = 1 if 'seconds' in request.GET.keys() else 0
        
                    dataset = MeteoData.objects.filter(date__range=(start, end))
                    gr = plot_graphic(
                        queryset=dataset, range=1, param=param, seconds=seconds)

            except ValidationError:
                message = "Данные введены неправильно"
                redirect('meteo-data')
        
        context = {
            'message': message,
            'user': request.user,
            'data': dataset,
            'graph': gr
        }
        return render(request, 'meteo_app/meteo_graph.html', context)
    return redirect('auth-page')


def create_wind_graph(request):
    if request.user.is_authenticated:
        dataset = None
        gr = False
        message = None
        if "date_from" in request.GET and "date_to" in request.GET:
            try:
                if request.GET["date_from"] and request.GET["date_from"] and request.GET["param"]:
                    start = request.GET["date_from"]
                    end = request.GET["date_to"]
                    param = request.GET["param"]
                    seconds = 1 if 'seconds' in request.GET.keys() else 0

                    dataset = WindData.objects.filter(date__range=(start, end))
                    gr = plot_graphic(
                        queryset=dataset, range=1, param=param, seconds=seconds)

            except ValidationError:
                message = "Данные введены неправильно"
                redirect('wind-data')

        context = {
            'message': message,
            'user': request.user,
            'data': dataset,
            'graph': gr
        }
        return render(request, 'meteo_app/wind_graph.html', context)
    return redirect('auth-page')


def create_invertor_graph(request):
    if request.user.is_authenticated:
        dataset = None
        gr = False
        message = None
        if "date_from" in request.GET and "date_to" in request.GET:
            try:
                if request.GET["date_from"] and request.GET["date_from"] and request.GET["param"]:
                    start = request.GET["date_from"]
                    end = request.GET["date_to"]
                    param = request.GET["param"]
                    seconds = 1 if 'seconds' in request.GET.keys() else 0

                    dataset = Invertor.objects.filter(date__range=(start, end))
                    gr = plot_graphic(
                        queryset=dataset, range=1, param=param, seconds=seconds)

            except ValidationError:
                message = "Данные введены неправильно"
                redirect('invertor-data')

        context = {
            'message': message,
            'user': request.user,
            'data': dataset,
            'graph': gr
        }
        return render(request, 'meteo_app/invertor_graph.html', context)
    return redirect('auth-page')

