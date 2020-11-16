# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from Task_4.district.central_street.house1 import room1 as cs_h1_r1, room2 as cs_h1_r2
from Task_4.district.central_street.house2 import room1 as cs_h2_r1, room2 as cs_h2_r2
from Task_4.district.soviet_street.house1 import room1 as ss_h1_r1, room2 as ss_h1_r2
from Task_4.district.soviet_street.house2 import room1 as ss_h2_r1, room2 as ss_h2_r2

COMMA = ', '
print('На районе живут:')

# for folk in room1.folks:
district_folks = COMMA.join(cs_h1_r1.folks)
district_folks += COMMA + COMMA.join(cs_h1_r2.folks)
district_folks += COMMA.join(cs_h2_r1.folks)
district_folks += COMMA + COMMA.join(cs_h2_r2.folks)
district_folks += COMMA + COMMA.join(ss_h1_r1.folks)
district_folks += COMMA + COMMA.join(ss_h1_r2.folks)
district_folks += COMMA + COMMA.join(ss_h2_r1.folks)
district_folks += COMMA + COMMA.join(ss_h2_r2.folks)

print(district_folks)
