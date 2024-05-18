sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
distances = {}
for city1, x1 in sites.items():
    distances[city1] = {}
    for city2, x2 in sites.items():
        if city1 != city2:
            distance = ((x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2) ** 0.5
            distances[city1][city2] = distance
print(distances)
