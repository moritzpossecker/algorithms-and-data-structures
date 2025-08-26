import vegas
import math
import matplotlib.pyplot as plt

def print_res(res):
    s1 = res.sdev
    s2 = res.mean
    print('geom. result volume = %.7f, mean result = %s, sdev = %.7f ' % (vol_exact, s2, s1))


# Parameter des Kegels
r = 1.0
h = 2.0

# analytisches Volumen
vol_exact = (1/3) * math.pi * r**2 * h


def f_cone(x):
    X, Y, Z = x
    if Z < 0 or Z > h:
        return 0.0
    r_z = r * (1 - Z/h)   # Radius in Höhe Z
    if X**2 + Y**2 <= r_z**2:
        #return math.cos(X**2 + Y**2 + Z**2)
        return 1.0
    else:
        return 0.0


# Daten für Iterationen sammeln
iters = list(range(10, 101, 10))
mean_iters = []
sdev_iters = []

for i in iters:
    integ = vegas.Integrator([[-1, 1], [-1, 1], [0, 2]])
    result = integ(f_cone, nitn=i, neval=6000)
    mean_iters.append(result.mean)
    sdev_iters.append(result.sdev)

# Daten für Evaluations sammeln
evals = list(range(1000, 10001, 1000))
mean_evals = []
sdev_evals = []

for i in evals:
    integ = vegas.Integrator([[-1, 1], [-1, 1], [0, 2]])
    result = integ(f_cone, nitn=40, neval=i)
    mean_evals.append(result.mean)
    sdev_evals.append(result.sdev)

# Plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot Iterationen
axes[0].errorbar(iters, mean_iters, yerr=sdev_iters, fmt='o-', capsize=5, label="MC Ergebnis")
axes[0].axhline(vol_exact, color='r', linestyle='--', label="Analytisch")
axes[0].set_xlabel("Anzahl Iterationen (neval=6000)")
axes[0].set_ylabel("Volumen")
axes[0].set_title("Einfluss der Iterationen")
axes[0].legend()

# Plot Evaluations
axes[1].errorbar(evals, mean_evals, yerr=sdev_evals, fmt='o-', capsize=5, label="MC Ergebnis")
axes[1].axhline(vol_exact, color='r', linestyle='--', label="Analytisch")
axes[1].set_xlabel("Anzahl Evaluationspunkte (nitn=40)")
axes[1].set_ylabel("Volumen")
axes[1].set_title("Einfluss der Evaluationspunkte")
axes[1].legend()

plt.tight_layout()
plt.show()
plt.savefig("vegas_plot.jpg")


print('Ohne vorgeschaltener Iterationsfolge:')
integ = vegas.Integrator([[-1, 1], [-1, 1], [0, 2]])
result = integ(f_cone, nitn=40, neval=6000)
print_res(result)

print('Mit vorgeschaltener Iterationsfolge:')
integ = vegas.Integrator([[-1, 1], [-1, 1], [0, 2]])
integ(f_cone, nitn=20, neval=6000)
result = integ(f_cone, nitn=40, neval=6000)
print_res(result)
