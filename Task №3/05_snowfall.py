# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
sd.resolution = (1600, 1000)

CONST_POWER_OF_GRAVITY = 20
CONST_MAX_POWER_OF_WIND = 10
CONST_SLEEP_TIME = 0.001


def random_snowflake_length(start, end):
    return sd.randint(start, end)


def power_of_wind(start, end):
    return sd.randint(start, end)


def snowflakes_down_draw(x, y, length, color):
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=length, color=color)


# def snowflakes_down(x, y, length):
def snowflakes_down(snowflakes_coords):
    while True:
        # sd.clear_screen()

        for i in range(len(snowflakes_coords)):
            x, y, length = snowflakes_coords[i][0], snowflakes_coords[i][1], snowflakes_coords[i][2]

            if y < length:
                continue

            sd.start_drawing()  # Всё, что рисуется далее, будет выведено на экран во время sd.finish_drawing()

            snowflakes_down_draw(x=x, y=y, length=length, color=sd.background_color)

            y -= CONST_POWER_OF_GRAVITY
            x = x + power_of_wind(-CONST_MAX_POWER_OF_WIND, CONST_MAX_POWER_OF_WIND)
            snowflakes_coords[i] = [x, y, length]

            snowflakes_down_draw(x=x, y=y, length=length, color=sd.COLOR_WHITE)

            sd.finish_drawing()  # Всё, что рисовали, начиная с sd.start_drawing(), будет выведено на экран здесь.

            sd.sleep(CONST_SLEEP_TIME)

        if y < length:
            break

        if sd.user_want_exit():
            break


rand_length_start = 10
rand_length_end = 100

snowflakes_coords = []

for _ in range(2):
    for _ in range(N):
        snowflake_length = random_snowflake_length(rand_length_start, rand_length_end)
        x_start = sd.random_number(snowflake_length, sd.resolution[0] - snowflake_length)

        snowflakes_coords.append([x_start, sd.resolution[1]-snowflake_length, snowflake_length])

    snowflakes_down(snowflakes_coords)

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
