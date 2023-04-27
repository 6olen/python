#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

import random
def draw_smiley(x, y, color):
    center = simple_draw.Point(x, y)
    radius = 50
    simple_draw.circle(center, radius, color, width=2)
    eye_radius = 10
    left_eye_center = simple_draw.Point(x - 20, y + 10)
    right_eye_center = simple_draw.Point(x + 20, y + 10)
    simple_draw.circle(left_eye_center, eye_radius, color, width=0)
    simple_draw.circle(right_eye_center, eye_radius, color, width=0)
    mouth_left = simple_draw.Point(x - 20, y - 20)
    mouth_right = simple_draw.Point(x + 20, y - 20)
    simple_draw.line(mouth_left, mouth_right, color, width=5)


for i in range(10):
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    color = simple_draw.random_color()
    draw_smiley(x, y, color)

simple_draw.pause()
