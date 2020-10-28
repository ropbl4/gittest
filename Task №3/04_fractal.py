# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код
sd.resolution = (1600, 1000)


def branch(point, angle, length, delta):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - delta
    next_length = length * .75
    branch(point=next_point, angle=next_angle, length=next_length, delta=delta)


point_0 = sd.get_point(300, 5)

for delta in range(0, 51, 10):
    branch(point=point_0, angle=90, length=150, delta=delta)
for delta in range(-50, 1, 10):
    branch(point=point_0, angle=90, length=150, delta=delta)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
def branch(point, angle, length, delta):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - delta
    koef_length_const = .75
    koef_length_start = koef_length_const - (koef_length_const / 100 * 20)  # -20%
    koef_length_end = koef_length_const + (koef_length_const / 100 * 20)    # +20%
    koef_length = sd.randint(int(koef_length_start * 100), int(koef_length_end * 100)) / 100
    next_length = length * koef_length
    branch(point=next_point, angle=next_angle, length=next_length, delta=delta)


point_0 = sd.get_point(1300, 5)

for delta in range(-90, 91, 30):
    rand_start = abs(delta) - (abs(delta) / 100 * 40)     # - 40%
    rand_end = abs(delta) + (abs(delta) / 100 * 40)       # + 40%
    delta_abs = sd.randint(int(rand_start), int(rand_end))

    if delta < 0:
        delta = -delta_abs
    else:
        delta = delta_abs

    branch(point=point_0, angle=90, length=150, delta=delta)

sd.pause()


