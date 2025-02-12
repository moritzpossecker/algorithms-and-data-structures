import random


def create_list(n: int) -> list:
    l = set()
    while len(l) < n:
        l.add(random.randint(0, n * 100))

    return list(l)
