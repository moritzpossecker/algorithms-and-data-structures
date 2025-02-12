from list_creator import create_list
import time
from sorting import bubble_sort


def get_average_sorting_time(list_size: int, runs: int) -> float:
    total_time = 0
    for i in range(runs):
        print('\tstarting run ' + str(i+1))
        l = create_list(list_size)
        start_time = time.process_time()
        bubble_sort(l)
        end_time = time.process_time()
        total_time += end_time - start_time

    return total_time / runs
