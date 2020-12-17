# -*- coding: utf-8 -*-

import simple_draw as sd
import Task_5.snowfall as sf

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

COUNT = 10
COLOR = sd.COLOR_WHITE

sf.create_snowflake(COUNT)

while True:
    sf.paint_all_snowflakes_with_color(color=sd.background_color)
    sf.move_snowflakes()
    sf.paint_all_snowflakes_with_color(color=COLOR)
    numbers = sf.numbers_of_snowflakes_out_of_screen()
    if numbers:
        sf.remove_snowflakes(numbers)
        sf.create_snowflake(len(numbers))

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
