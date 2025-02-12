def calc_fibonacci_rec(n: int) -> int:
    if n < 3:
        return 1

    return calc_fibonacci_rec(n - 1) + calc_fibonacci_rec(n - 2)

def calc_fibonacci_it(n: int) -> int:
    if n < 3:
        return 1

    last_num = 1
    res = 1
    for i in range(2, n):
        old_res = res
        res = last_num + res
        last_num = old_res

    return res
