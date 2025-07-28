import numpy as np

def f(x: float):
    return (np.tan(x) -x) / np.power(x, 3)

for k in range(1, 11):
    print('k:', k)
    x = 1 / np.power(10, k)
    print('x:', x)
    print('tan(x)', np.tan(x))
    print('f(x):', f(x))