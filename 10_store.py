#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
lamps = store[goods['Лампа']][0]['quantity']
lamps_cost = lamps * store[goods['Лампа']][0]['price']
print('Лампы -', lamps, 'шт, стоимость:', lamps_cost, 'руб')

table1 = store[goods['Стол']][0]['quantity']
table1_cost = table1 * store[goods['Стол']][0]['price']
table2 = store[goods['Стол']][1]['quantity']
table2_cost = table2 * store[goods['Стол']][1]['price']
print('Столы -', table1 + table2, 'шт, стоимость:', table1_cost + table2_cost, 'руб')

sofa1 = store[goods['Диван']][0]['quantity']
sofa1_cost = sofa1 * store[goods['Диван']][0]['price']
sofa2 = store[goods['Диван']][1]['quantity']
sofa2_cost = sofa2 * store[goods['Диван']][1]['price']
print('Диваны -', sofa1 + sofa2, 'шт, стоимость:', sofa1_cost + sofa2_cost, 'руб')

chair1 = store[goods['Стул']][0]['quantity']
chair1_cost = chair1 * store[goods['Стул']][0]['price']
chair2 = store[goods['Стул']][1]['quantity']
chair2_cost = chair2 * store[goods['Стул']][1]['price']
chair3 = store[goods['Стул']][2]['quantity']
chair3_cost = chair3 * store[goods['Стул']][2]['price']
print('Стулья -', chair1 + chair2 + chair3, 'шт, стоимость:', chair1_cost + chair2_cost + chair3_cost, 'руб')


##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






