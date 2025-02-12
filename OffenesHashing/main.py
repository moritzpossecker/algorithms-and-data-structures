import random
from math import ceil

from matplotlib import pyplot as plt

def get_hash_value(k, l):
    return k % l

def create_keys(low_bound, high_bound, l):
    s = set()
    while len(s) < l:
        s.add(random.randint(low_bound, high_bound + 1))

    return list(s)

def s_linear(h, tries):
    return h + tries

def s_quad(h, tries):
    return h - ceil(tries/2)**2 * (-1)**tries

def insert_key(k, hashlist, s_func = s_linear, hash_func = get_hash_value):
    l = len(hashlist)
    h = hash_func(k, l)
    try_num = 1
    while hashlist[h] is not None and try_num < l:
        h = hash_func(s_func(k, try_num), l)
        try_num += 1
    hashlist[h] = k
    return try_num - 1

key_list = create_keys(1, 10 ** 6, 4900)
hash_list_lin = [None for i in range(5001)]
hash_list_quad = [None for j in range(5001)]

linear_s_count = 0
quad_s_count = 0

for key in key_list:
    linear_s_count += insert_key(key, hash_list_lin, s_func=s_linear)

for key in key_list:
    quad_s_count += insert_key(key, hash_list_quad, s_func=s_quad)

for key in key_list:
    assert(key in hash_list_lin)
    assert(key in hash_list_quad)

print('Lineare Sondierungsaufrufe: ' + str(linear_s_count))
print('Quadratische Sondierungsaufrufe: ' + str(quad_s_count))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow([[1 if slot is not None else 0 for slot in hash_list_lin]], cmap="Greys", aspect="auto")
plt.title("Lineare Sondierung")
plt.xlabel("Index der Tabelle")
plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow([[1 if slot is not None else 0 for slot in hash_list_quad]], cmap="Greys", aspect="auto")
plt.title("Quadratische Sondierung")
plt.xlabel("Index der Tabelle")
plt.yticks([])

plt.tight_layout()
plt.show()
