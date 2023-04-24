#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код

zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код

for bird in birds:
    zoo.append(bird)
print(zoo)

# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код

zoo.remove('elephant')
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код

index_lion = zoo.index('lion') + 1
index_lark = zoo.index('lark') + 1
print(f"Лев находится в клетке: {index_lion}")
print(f"Жаворонок находится в клетке: {index_lark}")