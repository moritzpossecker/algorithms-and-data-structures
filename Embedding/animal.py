import math


class Animal:
    def __init__(self, name: str, species: int, size: float):
        self.name = name
        self.species = species
        self.size = size

    def vector(self):
        return [self.species * 0.5, math.log(self.size, 2000)]

    def connection_vector(self, target_vector: [float, float]) -> [float, float]:
        start_vector = self.vector()
        return [target_vector[0] - start_vector[0], target_vector[1] - start_vector[1]]

    def add_vector(self, vector: [float, float]) -> [float, float]:
        return [self.vector()[0] + vector[0], self.vector()[1] + vector[1]]

    def distance(self, animal_vector: [float, float]) -> float:
        connection_vector = self.connection_vector(animal_vector)
        return math.sqrt(connection_vector[0] ** 2 + connection_vector[1] ** 2)

    def similarity(self, animal_vector: [float, float]) -> float:
        return self.vector()[0] * animal_vector[0] + self.vector()[1] * animal_vector[1]
