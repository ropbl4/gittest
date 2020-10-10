# -*- coding: utf-8 -*-
import random
import simple_draw as sd

sd.resolution = (1200, 900)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
point = sd.get_point(100, 100)  # точка на полотне (x, y)
radius = 50

for _ in range(3):
    sd.circle(center_position=point, radius=radius)  # рисуем круг с центром в точке center_position и радиусом radius
    radius += 5


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def bubble(point, step, color=sd.COLOR_YELLOW):
    radius = 50
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, color=color, width=2)  # тут ещё ширина линии width пикселей
        radius += step


# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for i in range(100, 1001, 100):
    point = sd.get_point(i, 800)
    bubble(point=point, step=10)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
for i in range(100, 1001, 100):
    for j in range(300, 501, 100):
        point = sd.get_point(i, j)
        bubble(point=point, step=10)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point, step, sd.random_color())

sd.pause()
