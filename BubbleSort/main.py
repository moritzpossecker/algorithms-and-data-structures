import numpy as np
from sorting_timer import get_average_sorting_time
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def quadratic_fit(x, a, b, c):
    return a * x * x + b * x + c


def create_graph(x_data, y_data):
    plt.plot(x_data, y_data, label='data')
    popt, pcov = curve_fit(quadratic_fit, x_data, y_data)
    plt.plot(x_data, quadratic_fit(x_data, *popt), label='fit')
    plt.ylabel('time (in seconds)')
    plt.xlabel('size of list')
    plt.legend()
    # plt.savefig("graph.png")
    plt.show()

list_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
average_times = list()

for size in list_sizes:
    print('starting size ' + str(size))
    average_times.append(get_average_sorting_time(size, 10))

np_x_data = np.array(list_sizes)
np_y_data = np.array(average_times)

create_graph(np_x_data, np_y_data)
