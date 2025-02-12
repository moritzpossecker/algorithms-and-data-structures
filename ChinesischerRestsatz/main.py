from euklidischer_algo import get_s

b_i = [2, 3, 2]
m_i = [3, 5, 7]

def calc_m():
    m = m_i[0]
    for i in range(1, len(m_i)):
        m *= m_i[i]
    return m

M = calc_m()

def calc_as():
    a = []
    for m in m_i:
        a.append(int(M/m))
    return a

a_i = calc_as()

s_i = []

for j in range(len(a_i)):
    s_i.append(get_s(m_i[j], a_i[j]))

e_i = []
for j in range(len(a_i)):
    e_i.append(s_i[j] * a_i[j])

x = 0

for j in range(len(e_i)):
    x += e_i[j] * b_i[j]

print(x % M)
