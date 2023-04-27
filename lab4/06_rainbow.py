#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_point = sd.get_point(50, 50)
end_point = sd.get_point(350, 450)
line_width = 4
step = 5

for color in rainbow_colors:
    start_point.y -= step
    end_point.y -= step
    sd.line(start_point, end_point, color, line_width)
sd.pause()
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
radius = 550
center_position = sd.get_point(sd.resolution[0] // 2, -radius * 0.2)
line_width = 0

for color in rainbow_colors:
    radius += 10
    line_width += 5
    sd.circle(center_position, radius, color, line_width)

sd.pause()
