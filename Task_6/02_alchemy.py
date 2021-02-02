# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return 'Шторм'
        elif isinstance(other, Fire):
            return 'Пар'
        elif isinstance(other, Earth):
            return 'Грязь'
        elif isinstance(other, Ice):
            return 'Сосулька'
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return 'Шторм'
        elif isinstance(other, Fire):
            return 'Молния'
        elif isinstance(other, Earth):
            return 'Пыль'
        elif isinstance(other, Ice):
            return 'Сталактит'
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return 'Пар'
        elif isinstance(other, Air):
            return 'Молния'
        elif isinstance(other, Earth):
            return 'Лава'
        elif isinstance(other, Ice):
            return 'Талая вода'
        else:
            return None


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return 'Грязь'
        elif isinstance(other, Air):
            return 'Пыль'
        elif isinstance(other, Fire):
            return 'Лава'
        elif isinstance(other, Ice):
            return 'Грязный лёд'
        else:
            return None


print(Water(), '+', Air(), '=', Water() + Air())
print(Air(), '+', Water(), '=', Air() + Water())
print(Earth(), '+', Fire(), '=', Earth() + Fire())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
class Ice:
    def __str__(self):
        return 'Лёд'

    def __add__(self, other):
        if isinstance(other, Water):
            return 'Сосулька'
        elif isinstance(other, Air):
            return 'Сталактит'
        elif isinstance(other, Fire):
            return 'Талая вода'
        elif isinstance(other, Earth):
            return 'Грязный лёд'
        else:
            return None


print(Ice(), '+', Fire(), '=', Ice() + Fire())
print(Earth(), '+', Ice(), '=', Earth() + Ice())
