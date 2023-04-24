#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

brick_width = 100
brick_height = 50
wall_width = 800
wall_height = 600


for y in range(0, wall_height, brick_height):
    row_offset = (y // brick_height) % 2  
    for x in range(-brick_width, wall_width, brick_width):
        left_bottom = simple_draw.Point(x + row_offset * brick_width, y)
        right_top = simple_draw.Point(x + brick_width + row_offset * brick_width, y + brick_height)
        simple_draw.rectangle(left_bottom, right_top, width=1)

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

simple_draw.pause()
