import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from animal import Animal
from matplotlib import pyplot
import math


def get_mean_vector(animals: list[Animal]) -> [float, float]:
    mean = [0, 0]
    for animal in animals:
        mean[0] += animal.vector()[0]
        mean[1] += animal.vector()[1]

    return [mean[0] / len(animals), mean[1] / len(animals)]


def normalize_vector(vector) -> [float, float]:
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    return [vector[0] / length, vector[1] / length]

def animal_plot_vectors(all_animals: list[Animal]) -> list[[float, float]]:
    vectors = []
    mean_vector = get_mean_vector(all_animals)

    for animal in all_animals:
        centralized_vector = [animal.vector()[0] - mean_vector[0], animal.vector()[1] - mean_vector[1]]
        plot_vector = normalize_vector(centralized_vector)
        vectors.append(plot_vector)

    return vectors

def plot(animals: list[Animal]):
    fig, ax = pyplot.subplots()
    all_vectors = animal_plot_vectors(animals)
    x_values, y_values = zip(*all_vectors)
    ax.scatter(x_values, y_values, color='blue')

    for i in range(0, len(animals)):
        ax.annotate(animals[i].name,
                    xy=(x_values[i], y_values[i]),
                    textcoords='offset points',
                    ha='center',
                    fontsize=9,
                    xytext=(5,5))
    unit_circle = Circle((0,0), 1, edgecolor='red', facecolor='none', linestyle='--', linewidth=2, label='Einheitskreis')
    ax.add_patch(unit_circle)

    ax.set_xlabel('Dimension 1')
    ax.set_ylabel('Dimension 2')
    ax.set_title('Punktwolke der Tiere mit Einheitskreis')
    ax.grid(True)

    ax.set_aspect('equal', adjustable='datalim')
    plt.legend()
    #plt.savefig('animal_plot.png')
    plt.show()
