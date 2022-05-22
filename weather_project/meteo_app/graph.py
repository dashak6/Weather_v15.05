import matplotlib.pyplot as plt
from meteo_app.models import WindData




def plot_graphic():
    dataset = WindData.objects.all()

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim([0, 21])
    ax.set_xlabel("Дата")
    ax.set_ylabel("Скорость ветра")
    ax.set_title("Это тайтл")

    x_dots = [str(data.date) for data in dataset]
    x_dots = x_dots[:20]

    y_dots = [str(data.WS1AVG) for data in dataset]
    y_dots = y_dots[:20]

    ax.plot(x_dots, y_dots, color='blue', label='Изменение ветра')
    
    ax.legend()
    plt.show()
