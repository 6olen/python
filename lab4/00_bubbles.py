#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код

point = sd.get_point(100, 200)
radius = 30
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код

def draw_bubble(point, step, color):
    radius = 30
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)
point = sd.get_point(1050, 200)
draw_bubble(point, step=10, color=sd.COLOR_GREEN)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

def draw_bubble(point, step, color):
    radius = 40
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)
x = 150
y = 450
step = 7
for i in range(10):
    point = sd.get_point(x, y)
    draw_bubble(point, step, sd.random_color())
    x += 100
    
# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

def draw_bubble(point, step, color):
    radius = 25
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)

x = 250
y = 270
step = 3
for j in range(3):
    for i in range(10):
        point = sd.get_point(x, y)
        draw_bubble(point, step, sd.random_color())
        x += 70
    x = 250
    y -= 70

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

def draw_bubble(point, step, color):
    radius = 55
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)

for i in range(100):
    point = sd.random_point()
    draw_bubble(point, step=15, color=sd.random_color())  

sd.pause()