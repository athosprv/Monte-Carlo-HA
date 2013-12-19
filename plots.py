import cStringIO
from matplotlib.backends.backend_agg import *
from matplotlib.figure import *

def plot(data,filename='plot.png'):
    fig = Figure()
    axis = fig.add_subplot(111)
    for key,series in data.items():
        xs = [p[0] for p in series]
        ys = [p[1] for p in series]
        axis.plot(xs,ys)
    stream = open(filename,'wb')
    FigureCanvasAgg(fig).print_png(stream)
    return filename

def hist(data,filename='plot.png'):
    fig = Figure()
    axis = fig.add_subplot(111)
    if isinstance(data[0],list):
        for d in data:
            axis.hist(d, 25)
    else:
        axis.hist(data, 25)
    stream = open(filename,'wb')
    FigureCanvasAgg(fig).print_png(stream)
    return filename

if __name__=='__main__':
    import random
    plot(dict(squares=[(0,0),(1,1),(2,4),(3,9)]))
    hist([random.random() for i in range(1000)])
