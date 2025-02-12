from point_generator import generate_points
from point_calculator import distance
import random
import copy
from math import exp
from matplotlib import pyplot as plt


def e(point_order: list) -> float:
    dist = 0
    for i in range(1, len(point_order)):
        p1 = point_order[i - 1]
        p2 = point_order[i]
        dist += distance(p1, p2)

    p_last = point_order[len(point_order) - 1]
    p_first =point_order[0]
    dist += distance(p_last, p_first)
    return dist


def swap_points(point_order: list) -> list:
    i1 = random.randint(0, len(point_order) - 1)
    i2 = random.randint(0, len(point_order) - 1)
    while i1 == i2:
        i2 = random.randint(0, len(point_order) - 1)

    new_point_order = copy.deepcopy(point_order)
    new_point_order[i1] = point_order[i2]
    new_point_order[i2] = point_order[i1]
    return new_point_order


point_order_0 = generate_points(10)
best_order = point_order_0
T = 1000
decay = 0.9999
k_max = 300000
E_0 = e(point_order_0)
iterations = 0
its_wo_change = 0

for k in range(0, k_max):
    point_order_1 = swap_points(point_order_0)
    E_1 = e(point_order_1)
    d_E: float = E_1 - E_0
    if d_E < 0:
        point_order_0 = copy.deepcopy(point_order_1)
        best_order = copy.deepcopy(point_order_1)
        E_0 = E_1
        its_wo_change = 0
    else:
        p = exp(-(d_E / T))
        if p > random.random():
            point_order_0 = copy.deepcopy(point_order_1)
            E_0 = E_1
            its_wo_change = 0
        else:
            its_wo_change += 1

    if its_wo_change > 500:
        break

    iterations += 1
    T *= decay

ordered_x = []
ordered_y = []

for point in best_order:
    ordered_x.append(point[0])
    ordered_y.append(point[1])

ordered_x.append(best_order[0][0])
ordered_y.append(best_order[0][1])

plt.suptitle('Simulated Annealing')
plt.title('Iterations: ' + str(iterations) + ' Distance: ' + str(round(e(best_order), 2)))
plt.plot(ordered_x, ordered_y, '.')
plt.plot(ordered_x, ordered_y)
# plt.savefig('simulated_annealing_graph.png')
plt.show()
