from time import perf_counter_ns
from fibonacci import calc_fibonacci_rec, calc_fibonacci_it


def time_fibonacci(n):
    start_time = perf_counter_ns()
    calc_fibonacci_rec(n)
    end_time = perf_counter_ns()
    rec_time = end_time - start_time

    start_time = perf_counter_ns()
    calc_fibonacci_it(n)
    end_time = perf_counter_ns()

    it_time = end_time - start_time

    return rec_time, it_time