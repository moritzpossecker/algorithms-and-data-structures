from animal import Animal
from animal_plot import plot

animals = [Animal("Elefant", -1, 3600),
           Animal("Giraffe", -1, 1600),
           Animal("Löwe", -1, 200),
           Animal("Panther", -1, 60),
           Animal("Hund", -1, 20),
           Animal("Ratte", -1, 0.2),
           Animal("Maus", -1, 0.025),
           Animal("Walhei", 1, 17000),
           Animal("Thunfisch", 1, 100),
           Animal("Forelle", 1, 1),
           Animal("Clownfisch", 1, 0.2),
           Animal("Hering", 1, 0.2),
           Animal("Seepferdchen", 1, 0.015),]

plot(animals)

elefant = animals[0]
mouse = animals[6]
clownfish = animals[10]

compare_vector = mouse.connection_vector(elefant.vector())
result_vector = clownfish.add_vector(compare_vector)

max_similarity = animals[0].similarity(result_vector)
most_similar_animal = animals[0]

for i in range(1, len(animals)):
    similarity = animals[i].similarity(result_vector)
    if similarity > max_similarity:
        max_similarity = similarity
        most_similar_animal = animals[i]

print(most_similar_animal.name)
print('Similarity: ' + str(max_similarity))