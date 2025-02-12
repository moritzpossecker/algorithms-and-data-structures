from fibonacci import calc_fibonacci_it, calc_fibonacci_rec
import matplotlib.pyplot as plt
from time_fibonacci import time_fibonacci
from scipy.optimize import curve_fit


def compare_fib_nums():
    for fib_num in range(3, 31):
        it_num = calc_fibonacci_it(fib_num)
        rec_num = calc_fibonacci_rec(fib_num)
        if it_num != rec_num:
            print("Unterschied gefunden:")
            print(str(fib_num) + ': Iterativ: ' + str(it_num) + ' Rekursiv: ' + str(rec_num))


def exponential_fit(x, a, b):
    return a * b**x

def create_graph(x_data, y_data_rec, y_data_it):
    plt.plot(x_data, y_data_rec, label='recursive')
    plt.plot(x_data, y_data_it, label='iterative')
    popt, pcov = curve_fit(exponential_fit, x_data, y_data_rec)
    plt.plot(x_data, exponential_fit(x_data, *popt), label=f'fit: f(x)={round(popt[0], 3)} * {round(popt[1], 2)} ^ x')
    plt.ylabel('time (in nanoseconds)')
    plt.xlabel('size of list')
    plt.legend()
    # plt.savefig("graph.png")
    plt.show()


fib_nums = list()
rec_times = list()
it_times = list()

for fib_num in range(3, 31):
    fib_nums.append(fib_num)
    rec_time, it_time = time_fibonacci(fib_num)
    rec_times.append(rec_time)
    it_times.append(it_time)

create_graph(fib_nums, rec_times, it_times)