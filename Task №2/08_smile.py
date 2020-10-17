# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
import random

sd.resolution = (1350, 950)
radius = 100


def smile(x, y, color):
    width = 2
    shift_eye_x = 60
    shift_eye_y = 20
    shift_eye_up_x = 10
    shift_eye_up_y = 10
    shift_mouth_y = 20

    # Head
    sd.circle(center_position=sd.get_point(x, y), radius=radius, color=color, width=width)

    # Left eye
    point_start = sd.get_point(x - shift_eye_x, y + shift_eye_y)
    point_end = sd.get_point(x - shift_eye_x + shift_eye_up_x, y + shift_eye_y + shift_eye_up_y)
    sd.line(point_start, point_end, color=color, width=width)

    point_start = sd.get_point(x - shift_eye_x + shift_eye_up_x, y + shift_eye_y + shift_eye_up_y)
    point_end = sd.get_point(x - shift_eye_x + shift_eye_up_x * 2, y + shift_eye_y)
    sd.line(point_start, point_end, color=color, width=width)

    # Right eye
    point_start = sd.get_point(x + shift_eye_x, y + shift_eye_y)
    point_end = sd.get_point(x + shift_eye_x - shift_eye_up_x, y + shift_eye_y + shift_eye_up_y)
    sd.line(point_start, point_end, color=color, width=width)

    point_start = sd.get_point(x + shift_eye_x - shift_eye_up_x, y + shift_eye_y + shift_eye_up_y)
    point_end = sd.get_point(x + shift_eye_x - shift_eye_up_x * 2, y + shift_eye_y)
    sd.line(point_start, point_end, color=color, width=width)

    # Mouth
    point_start = sd.get_point(x - shift_eye_x + shift_eye_up_x * 3, y - shift_mouth_y)
    point_end = sd.get_point(x + shift_eye_x - shift_eye_up_x * 3, y - shift_mouth_y)
    sd.line(point_start, point_end, color=color, width=width)


for _ in range(10):
    x = random.randint(1, sd.resolution[0]//radius//2)
    y = random.randint(1, sd.resolution[1]//radius//2)
    print(x, y)
    smile(x*radius*2, y*radius*2, sd.COLOR_YELLOW)

# point = sd.random_point()
# smile(point.x, point.y, sd.COLOR_YELLOW)

sd.pause()
