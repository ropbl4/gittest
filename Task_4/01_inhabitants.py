# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код
import Task_4.room_1
from Task_4 import room_2
from Task_4.room_3 import folks

# import .room_1            # так не работает
# from . import room_2      # так можно
# from .room_3 import folks # так можно

print('В комнате room_1 живут: ')

for folk in Task_4.room_1.folks:
    print(folk)

print('\nВ комнате room_2 живёт: ')

for folk in room_2.folks:
    print(folk)

print('\nВ комнате room_3 живёт: ')

for folk in folks:
    print(folk)
