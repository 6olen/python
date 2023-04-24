#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря

for city1 in sites:
    for city2 in sites:
        if city1 != city2 and distances.get((city2, city1)) is None:
            x1, y1 = sites[city1]
            x2, y2 = sites[city2]
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            distances[(city1, city2)] = distance

for (city1, city2), distance in distances.items():
    print(f"{city1} - {city2}: {distance:.2f}")

#print(distances)





