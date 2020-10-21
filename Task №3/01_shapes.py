# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1600, 1000)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код
length = 200
point = sd.get_point(100, 100)

# v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
# v1.draw()
#
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# v2.draw()
#
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# v3.draw()


def triangle(point, angle=0, length=200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()


point_0 = sd.get_point(100, 100)

for angle in range(0, 361, 90):
    triangle(point=point_0, angle=angle, length=100)

# ------------------------------------------------------


def square(point, angle=90, length=200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 270, length=length, width=3)
    v3.draw()


point_0 = sd.get_point(300, 300)

for angle in range(0, 361, 90):
    square(point=point_0, angle=angle, length=100)

# ------------------------------------------------------


def fiveangle(point, angle=90, length=200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw()

    v3 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v3.draw()

    v3 = sd.get_vector(start_point=v3.end_point, angle=angle + 288, length=length, width=3)
    v3.draw()


point_0 = sd.get_point(500, 500)

# for angle in range(0, 361, 72):
fiveangle(point=point_0, angle=0, length=100)

# ------------------------------------------------------


def sixangle(point, angle=90, length=200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw()

    v3 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v3.draw()

    v3 = sd.get_vector(start_point=v3.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()

    v3 = sd.get_vector(start_point=v3.end_point, angle=angle + 300, length=length, width=3)
    v3.draw()


point_0 = sd.get_point(700, 700)

# for angle in range(0, 361, 72):
sixangle(point=point_0, angle=0, length=100)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

# ------------------------------------------------------

def parallelogramm(point, count_of_angles, start_angle=0, length=200):
    angle_between_lines = 360 / count_of_angles
    angle_sum = start_angle

    for _ in range(count_of_angles):
        point = parallelogramm_draw(point, angle_sum, length)
        angle_sum += angle_between_lines


def parallelogramm_draw(point, angle=0, length=200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    return v1.end_point


point_0 = sd.get_point(900, 500)
count_of_angles = 6
angle = 0

for angle in range(0, 361, 360 // count_of_angles):
    parallelogramm(point=point_0, count_of_angles=count_of_angles, start_angle=angle, length=100)


sd.pause()
