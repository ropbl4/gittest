#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)
in_garden_or_meadow = garden_set | meadow_set

# выведите на консоль все виды цветов
# TODO здесь ваш код
print(in_garden_or_meadow)

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
in_garden_and_meadow = garden_set & meadow_set
print(in_garden_and_meadow)

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
in_garden_but_not_in_meadow = garden_set - meadow_set
print(in_garden_but_not_in_meadow)

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
in_meadow_but_not_in_garden = meadow_set - garden_set
print(in_meadow_but_not_in_garden)


