def get_s(m, a):
    q_list = get_q(m, a)
    r_i = 0
    s_i = 1
    for i in range(len(q_list) - 2, 1, -1):
        new_s = r_i - (q_list[i] * s_i)
        r_i = s_i
        s_i = new_s

    return s_i % m

def get_q(m, a):
    q_list = []
    current_m = m
    current_a = a
    while True:
        q = int(current_m / current_a)
        r = current_m - (q * current_a)
        current_m = current_a
        current_a = r
        q_list.append(q)
        if r == 0:
            break

    return q_list
