import matplotlib.pyplot as plt
from meteo_app.models import MeteoData

def plot_graphic(queryset=None, range=10, param=None):
    if queryset:
        try:
            x = list()
            y = list()
            
            dataset = [(d.date, getattr(d, param)) for d in queryset]
            for i, d in enumerate(dataset):
                if i % range == 0:
                    x.append(d['date'].strftime('%Y-%m-%d %H:%M'))
                    y.append(d[param])
                

            fig = plt.figure()
            fig.set_figheight(12)
            fig.set_figwidth(10)
            
            ax = fig.add_subplot()
            ax.set_xlim([0, len(x) + 1])
            ax.set_xlim([0, len(y) + 1])
            
            ax.set_xlabel("Дата")
            ax.set_ylabel("Среднее значение температуры")
            ax.set_title("Это тайтл")


            ax.plot(x, y, color='blue', label='Температура')
            plt.xticks(rotation=30, fontsize=10)
            ax.legend()

            plt.savefig('meteo_app/images/graph.png', dpi=100)
            
            return True
        except:
            return False
    else:
        return False
