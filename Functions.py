def vector_module(x, y, *, z):  # требуем указать параметр z явно
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# res = vector_module(2, 3, 4)      # не сработает
res = vector_module(2, 3, z=4)    # сработает
print(res)


def vector_module(*, x, y, z):  # требуем указать параметр z явно
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# res = vector_module(2, 3, 4)      # не сработает
# res = vector_module(2, 3, z=4)    # не сработает
res = vector_module(x=2, y=3, z=4)    # сработает
print(res)


def vector_module(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# res = vector_module(2, y=3, 4)    # не сработает: если начал именовать параметры - продолжай

# ------------------------------

# распаковка позиционных параметров
some_list = [2, 3, 4]
res = vector_module(*some_list)     # вместо (some_list[0], some_list[1], some_list[2])
print(res)

some_dict = {'x': 2, 'y': 3, 'z': 4}
res = vector_module(**some_dict)    # вместо (some_dict['x'], some_dict['y'], some_dict['z'])
print(res)

some_list = [2, 3]
some_dict = {'z': 4}
res = vector_module(*some_list, **some_dict)     # так тоже можно
print(res)


# ------------------------------

# значения по умолчанию вычисляются в точке определения функции, при компиляции
# обычная ошибка - изменяемый обьект в качестве параметра по умолчанию
def add_element_to_list(element, list_to_add=[]):
    """добавляем элемент к списку"""
    list_to_add.append(element)
    return list_to_add


my_list = [3, 4, 5]
add_element_to_list(element=1, list_to_add=my_list)
print(my_list)

new_list = add_element_to_list(element=1)
print(new_list)
add_element_to_list(element=7, list_to_add=new_list)
print(new_list)

other_new_list = add_element_to_list(element=2)
print(other_new_list)
print(new_list)
print(new_list is other_new_list)


# решение проблемы
def add_element_to_list(element, list_to_add=None):
    """добавляем элемент к списку"""
    if list_to_add is None:
        list_to_add = []
    list_to_add.append(element)
    return list_to_add


my_list = [3, 4, 5]
add_element_to_list(element=1, list_to_add=my_list)
print(my_list)

new_list = add_element_to_list(element=1)
print(new_list)
add_element_to_list(element=7, list_to_add=new_list)
print(new_list)

other_new_list = add_element_to_list(element=2)
print(other_new_list)
print(new_list)
print(new_list is other_new_list)


# Произвольное число параметров
print(1, 2, 3, 4, 5, 56, 6,)


# ------------------------------

# Произвольное число позиционных параметров
def print_them_all_v1(*args):
    print('print_them_all_v1')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)


print_them_all_v1(2, 'привет', 5.6)

# распаковка
my_favorite_pets = ['lion', 'elephant', 'monkey', 'cat', 'horse']
print_them_all_v1(my_favorite_pets)
print_them_all_v1(*my_favorite_pets)

# Произвольное число именованных параметров
def print_them_all_v2(**kwargs):
    print('print_them_all_v2')
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


print_them_all_v2(name='Вася', address='Moscow', home=42)

# распаковка
my_friend = {'name': 'Вася', 'address': 'Moscow', 'age': 25}
print_them_all_v2(**my_friend)

# неправильные вызовы
# print_them_all_v1(name='Вася', address='Moscow')  # в неименованные параметры нельзя подставлять именованные
# print_them_all_v2('Вася', 'Moscow', 25)   # в именованные параметры нельзя подставлять неименованные


# Комбинация
def print_them_all_v3(*args, **kwargs):
    print('print_them_all_v3')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


print_them_all_v3('Вася', 'Moscow', 25)
print_them_all_v3(name='Вася', address='Moscow')

print_them_all_v3(1000, 'рублей', name='Вася', address='Moscow')

my_friend = {'name': 'Вася', 'address': 'Moscow'}
print_them_all_v3(1000, 'рублей', **my_friend)


# При создании функции можно указывать как обычные параметры, так и произвольные параметры
def print_them_all_v4(a, b=5, *args, **kwargs):
    print('print_them_all_v4')
    print('a и b:', a, b)
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


print_them_all_v4(5, 6, 7, 8, cat='мяу!')
print_them_all_v4(5, b=8, cat='мяу!')
print_them_all_v4(5, cat='мяу!', address='Moscow')
