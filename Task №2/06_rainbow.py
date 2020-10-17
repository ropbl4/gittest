# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

for i in range(7):
    point_start = sd.get_point(50+5*i, 50)
    point_end = sd.get_point(350+5*i, 450)
    sd.line(start_point=point_start, end_point=point_end, color=rainbow_colors[i], width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
point = sd.get_point(80, 0)

for i in range(7):
    radius = 50 + 5 * i
    sd.circle(center_position=point, radius=radius, color=rainbow_colors[i], width=4)

sd.pause()
