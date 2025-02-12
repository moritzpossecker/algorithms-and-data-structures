import random

def generate_points(n: int, lower_bound: int = 0, upper_bound: int = 41) -> list:
    points = set()
    while len(points) < n:
        x = random.randint(lower_bound, upper_bound)
        y = random.randint(lower_bound, upper_bound)
        points.add((x, y))

    return list(points)