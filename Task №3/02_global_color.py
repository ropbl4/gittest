# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код
sd.resolution = (1600, 1000)
COLORS = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def parallelogramm(point, count_of_angles, start_angle=0, length=200, color=COLORS[2]):
    angle_between_lines = 360 / count_of_angles
    angle_sum = start_angle

    for _ in range(count_of_angles):
        point = parallelogramm_draw(point, angle_sum, length, color=color)
        angle_sum += angle_between_lines


def parallelogramm_draw(point, angle=0, length=200, color=COLORS[2]):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)
    return v1.end_point


point_0 = sd.get_point(900, 500)
count_of_angles = 6
angle = 0
color = int(input(f'Введите число 0-{len(COLORS)-1} (это выбор цвета): '))

for angle in range(0, 361, 360 // count_of_angles):
    parallelogramm(point=point_0, count_of_angles=count_of_angles, start_angle=angle, length=100, color=COLORS[color])

sd.pause()
