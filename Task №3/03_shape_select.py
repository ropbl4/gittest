# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код
sd.resolution = (1600, 1000)
COLORS = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
FIGURES = {3: 'Треугольник', 4: 'Квадрат', 5: '5-угольник', 6: '6-угольник'}

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
angle = 0

for i in FIGURES:
    print(i, '-', FIGURES[i])

figure = int(input(f'Введите число из списка выше (это выбор фигуры):'))
count_of_angles = figure

color = int(input(f'Введите число 0-{len(COLORS)-1} (это выбор цвета): '))

for angle in range(0, 361, 360 // count_of_angles):
    parallelogramm(point=point_0, count_of_angles=count_of_angles, start_angle=angle, length=100, color=COLORS[color])

sd.pause()
