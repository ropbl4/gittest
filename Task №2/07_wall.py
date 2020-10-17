# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
sd.resolution = (850, 500)
brick_width = 100
brick_height = 50

for i in range(7):
    for j in range(7):
        if j % 2 == 0:
            point_start = sd.get_point(50 + i*brick_width, 50 + j*brick_height)
            point_end = sd.get_point(150 + i*brick_width, 100 + j*brick_height)
        else:
            point_start = sd.get_point(50 + i * brick_width + brick_width/2, 50 + j * brick_height)
            point_end = sd.get_point(150 + i * brick_width + brick_width/2, 100 + j * brick_height)

        sd.rectangle(left_bottom=point_start, right_top=point_end, color=sd.COLOR_ORANGE, width=4)
        # sd.line(start_point=point_start, end_point=point_end, color=sd.COLOR_ORANGE, width=4)

sd.pause()
