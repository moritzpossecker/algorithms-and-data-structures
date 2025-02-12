def bubble_sort(a: list) -> list:
    for n in range(0, len(a) - 1):
        for j in range(1, len(a) - n):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]

    return a