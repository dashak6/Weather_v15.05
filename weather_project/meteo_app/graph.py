import matplotlib
import matplotlib.pyplot as plt
from meteo_app.models import MeteoData, WindData, Invertor

def plot_graphic(queryset=None, range=1, param=None, seconds=False):
    if queryset:
        x = list()
        y = list()
        
        dataset = [(d.date, getattr(d, param)) for d in queryset]
        if seconds:
            for i, d in enumerate(dataset):
                if i % range == 0:
                    x.append(d[0].strftime('%Y-%m-%d %H:%M:%S'))
                    y.append(d[1])
        else:
            xy = dict()
            for d in dataset:
                if d[0].strftime('%Y-%m-%d %H:%M') not in xy:
                    xy[d[0].strftime('%Y-%m-%d %H:%M')] = d[1]
            
            print(xy)
            for ax, ay in xy.items():
                x.append(ax)
                y.append(ay)

            
        matplotlib.use('Agg')
        fig = plt.figure()
        fig.set_figheight(12)
        fig.set_figwidth(10)
        
        ax = fig.add_subplot()

        ax.set_xlim([0, len(x) + 1])
        ax.set_xlim([0, len(y) + 1])
        
        ax.set_xlabel("Дата")
        ax.set_ylabel("Среднее значение температуры")
        ax.set_title("Это тайтл")
        
        if len(x) >= 25:
            ax.set_xticks([])
        if len(y) >= 25:
            ax.set_yticks([])

        ax.plot(x, y, color='blue', label='Температура')
        plt.xticks(rotation=30, fontsize=10)
        ax.legend()

        plt.savefig('meteo_app/static/meteo_app/graph.png', dpi=100)
        print('LOGGING: IMAGE CREATED')
        
        return True
    else:
        return False

