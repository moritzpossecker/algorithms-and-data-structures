import math
from copy import deepcopy

import numpy as np


def round_sig(x, sig=3):
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)


def exact_solution(A, B):
    return np.linalg.solve(A, B)


def solve_diagonal(A, B):
    factor = round_sig(A[1][0] / A[0][0])
    A[1][0] = 0
    A[1][1] = round_sig(A[1][1] - round_sig(factor * A[0][1]))
    B[1] = round_sig(B[1] - round_sig(factor * B[0]))

    x_2 = round_sig(B[1] / A[1][1])
    x_1 = round_sig(round_sig(B[0] - round_sig(x_2 * A[0][1])) / A[0][0])

    return x_1, x_2


def solve_column_max(A, B):
    if abs(A[1][0]) > abs(A[0][0]):
        A[0], A[1] = A[1], A[0]
        B[0], B[1] = B[1], B[0]

    return solve_diagonal(A, B)


MATRIX_A = [[0.035, 3.62], [1.17, 1.42]]
MATRIX_B = [9.12, 5.89]

print(exact_solution(MATRIX_A, MATRIX_B))
print('Diagonalstrategie: ' + str(solve_diagonal(deepcopy(MATRIX_A), deepcopy(MATRIX_B))))
print('Spaltenmaximumstrategie: ' + str(solve_column_max(deepcopy(MATRIX_A), deepcopy(MATRIX_B))))

