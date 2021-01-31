# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    # flakes_can_not_fall_count = 0

    def __init__(self, coord):
        self.coord = coord

    def clear_previous_picture(self):
        point = sd.get_point(self.coord[0], self.coord[1])
        sd.snowflake(center=point, length=self.coord[2], color=sd.background_color)

    def move(self):
        self.coord[1] -= self.coord[2]

    def draw(self):
        point = sd.get_point(self.coord[0], self.coord[1])
        sd.snowflake(center=point, length=self.coord[2])

    def can_fall(self):
        # если центр < 0, луч может торчать; чтобы скрыть луч, центр должен быть ниже нуля на длину луча
        if self.coord[1] < 0 - self.coord[2]:
            # self.flakes_can_not_fall_count += 1
            return False
        else:
            return True


# flake = Snowflake([300, 500, 20])
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
MIN_FLAKE_LEN, MAX_FLAKE_LEN = 5, 25
FLAKES_COUNT = 5


def get_flakes(count):
    flakes_coord = []
    for _ in range(count):
        length = sd.randint(MIN_FLAKE_LEN, MAX_FLAKE_LEN)
        x = sd.randint(0 + length, sd.resolution[1] - length)
        y = sd.resolution[0]
        # y = 100

        flakes_coord.append(Snowflake([x, y, length]))

    return flakes_coord


def get_fallen_flakes():
    fallen_flakes_count = 0

    for flake in flakes:
        if not flake.can_fall():
            fallen_flakes_count += 1
            flakes.remove(flake)

    return fallen_flakes_count


def append_flakes(count):
    list_of_flakes = get_flakes(count)

    for i in range(count):
        flakes.append(list_of_flakes[i])


flakes = get_flakes(FLAKES_COUNT)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подсчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
