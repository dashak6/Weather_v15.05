import csv
import xlsxwriter 
from django.core.paginator import Paginator


def model_data_to_csv(model, filename):
    dataobject = model.objects.all()
    # получение названий всех колонок (заголовок)
    headers = [str(data.name) for data in dataobject[0]._meta.fields]
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for obj in dataobject:
            # получение списка данных каждого объекта из кверисета
            # в соответствии с порядком заголовков
            data = [str(obj.__getattribute__(d)) for d in headers]
            writer.writerow(data)


def model_data_to_xls(model, filename):
    book = xlsxwriter.Workbook(filename)
    sheet = book.add_worksheet()
    row = 0
    column = 0
    dataobject = model.objects.all()
    headers = [str(data.name) for data in dataobject[0]._meta.fields]
    for header in headers:
        sheet.write(row, column, header)
        column += 1
    row += 1
    column = 0
    for obj in dataobject:
        data = [str(obj.__getattribute__(d)) for d in headers]
        for d in data:
            sheet.write(row, column, d)
            column += 1
        column = 0
        row += 1
    book.close()
    

def get_page_obj(request, size=100, model=None, queryset=None):
    
    dataset = model.objects.all() if model else queryset
    paginator = Paginator(dataset, size)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return page_obj
