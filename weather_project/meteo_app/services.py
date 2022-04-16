import csv
#import os
#from weather_project.settings import BASE_DIR
#from meteo_app.models import MeteoData, WindData


# def create_meteo_data_csv():
#     dataobject = MeteoData.objects.all()
#     headers = [str(data.name) for data in dataobject[0]._meta.fields]
#     filepath = os.path.join(str(BASE_DIR)+f"/meteo_app/files/meteo.csv")
#     with open(filepath, 'w') as file:
#         writer = csv.writer(file)
#         writer.writerow(headers)
#         for obj in dataobject:
#             data = [str(obj.__getattribute__(d)) for d in headers]
#             writer.writerow(data)


# def create_wind_data_csv():
#     dataobject = WindData.objects.all()
#     headers = [str(data.name) for data in dataobject[0]._meta.fields]
#     filepath = os.path.join(str(BASE_DIR)+"/meteo_app/files/wind.csv")
#     with open(filepath, 'w') as file:
#         writer = csv.writer(file)
#         writer.writerow(headers)
#         for obj in dataobject:
#             data = [str(obj.__getattribute__(d)) for d in headers]
#             writer.writerow(data)

def model_data_to_csv(model, filename):
    dataobject = model.objects.all()
    headers = [str(data.name) for data in dataobject[0]._meta.fields]
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for obj in dataobject:
            data = [str(obj.__getattribute__(d)) for d in headers]
            writer.writerow(data)
    