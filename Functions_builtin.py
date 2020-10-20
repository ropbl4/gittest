# abs() - абсолютное значение числа
print(abs(1))
print(abs(-1))

# round() - округление до нужного знака
print(round(3.1425926, 2))
print(round(3.1425926, 3))
print(round(3.1425926, 0))

# --- Cписки ---

profit = [100, 20, 5, 1200, 42, ]

# len() - размер списка
print(len(profit))

# max() - максимальный элемент
print(max(profit))

# min() - минимальный элемент
print(min(profit))

# sorted() - отсортированный список
print(sorted(profit))

# sum() - сумма элементов списка
print(sum(profit))

# zip() - попарная компоновка элементов двух списков
profit = [100, 20, 5, 1200, 42, ]
days = ['пн', 'вт', 'ср', 'чт', 'пт', ]
res = zip(profit, days, )
print(list(res))

# --- Логические ---
print('\n--- Логические ---')

# all() - True если ВСЕ элементы списка/множества True
print(all([True, True, True, True, ]))
print(all([1, 0, 1, ]))
print(all([1, '0', 1, ]))

# any() - True если ХОТЯ БЫ ОДИН элемент списка True
print(any([True, False, True, True, ]))
print(any([1, 0, None, ]))

# --- Интроспекция ---
print('\n--- Интроспекция ---')

# dir() - список всех аттрибутов обьекта
dir(profit)
dir([])

# help() - встроенная помощь по функции/обьекту
help(profit)
help(print)

# id() - внутренний идентификатор обьекта
a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
c = [1, 2, 3]
print(id(c))
print(a == b, a is b, id(a) == id(b))
print(a == c, a is c, id(a) == id(c))
print(id(None))
print(id(False))
print(id(True))

# --- Общего назначения ---
print('\n--- Общего назначения ---')

# hash() - значение хэша для обьекта. Что такое хэш-функции см https://goo.gl/gZLM4o
print(hash('Кржижановский'))
# hash(profit)  # только для неизменяемых типов
print(hash(tuple(profit)))

# isinstance() - является ли обьект обьектом данного класса
print(isinstance(profit, list))

# type() - тип(КЛАСС) обьекта
print(type(profit))

print('\n-------- Выводим содержание Conflicts.txt --------')
# open() - открыть файл на файловой системе
ff = open('Task №2/Conflicts.txt', 'r', encoding='UTF8')
for line in ff.readlines():
    print(line, end='')
ff.close()
