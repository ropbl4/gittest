a = int(3.0)
print(a)
a = float(5)
print(a)

a = 'qwerty' == 'qwerty'
print(a)
a = 'qwerty' > 'qwe'
print(a)
a = 'qwerty' < 'qwe'
print(a)

a = 'привет'.encode()
print(a)
a = b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode()
print(a)

a = 'qwerty'[0]
print(a)
a = 'qwerty'[-1]
print(a)
a = 'qwerty'[2:4]
print(a)

русское_имя_переменной = 23
print('русское_имя_переменной = ', русское_имя_переменной)

x, y, z = 100, 150, 200
print(f'x = {x}, y = {y}, z = {z}')

a = type(x)
print(a)
a = isinstance(x, int)
print(a)
a = isinstance(x, float)
print(a)
a = id(x)
print(a)
x = y
print(f'x id = {id(x)} \ny id = {id(y)}')

x = 'i am 2'
a = x.isalpha()     # все символы в переменной строковые ?
print(a)
x = 'i am two'
a = x.isalpha()
print(a)
x = 'i_am_two'
a = x.isalpha()
print(a)
x = 'iamtwo'
a = x.isalpha()
print(a)
a = x.isnumeric()
print(a)
x = '345'
a = x.isnumeric()
print(a)
print(x)
a = int(x)
print(a)

print('------------------')

my_list = [1, 2, 3, 'qwerty', 5]
print(my_list[2:])
my_list.append(6)   # добавили элемент в конец
print(my_list)
my_list.extend([7, 'aaa', 9])   # добавили целый список в конец
print(my_list)
my_list += [10, 11, 12]         # можно и так добавить
print(my_list)
my_list.insert(3, 'inserted element')
print(my_list)
del my_list[3]  # удалили элемент с индексом 3
print(my_list)
my_list.remove(5)   # удалили первое найденное значение "5"
print(my_list)
my_list = [1, x, z]     # можно и переменные
print(my_list)
my_list *= 3
print('my_list *= 3:', my_list)
a = my_list.count(200)  # количество вхождений элемента "200"
print('my_list.count(200):', a)
a = 1 in my_list    # 1 содержится в списке my_list ?
print('1 in my_list:', a)
a = 2 in my_list
print('2 in my_list:', a)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('matrix =', matrix)
print('matrix[1] =', matrix[1])
print('matrix[1][2] =', matrix[1][2])

a = [1, 2, 3] == [1, 2, 3]
print('[1, 2, 3] == [1, 2, 3]:', a)
a = [1, 2, 3] == [3, 2, 1]
print('[1, 2, 3] == [3, 2, 1]:', a)
a = [1, 2, 3] > [3, 2, 1]
print('[1, 2, 3] > [3, 2, 1]:', a)
a = [1, 2, 3] < [3, 2, 1]
print('[1, 2, 3] < [3, 2, 1]:', a)

a = min(matrix)
print('min(matrix) = ', a)
a = max(matrix)
print('max(matrix) = ', a)

my_list = [4, 2, 8, 5, 1]
my_list.sort()
print(my_list)

first_list = [1, 2, 3]
second_list = first_list
first_list[2] = 99
print(second_list)

print('------------------')

x = 10
y = x
print('id(x) = ', id(x))
print('id(y) = ', id(y))
y += 1
print('id(y) = ', id(y))
y -= 1
print('id(y) = ', id(y))


print('------ Словари --------')

my_dict = {}
print(my_dict)
my_dict['машина'] = 'Citroen'
my_dict['слон'] = 'Elephant'
print(my_dict)
print("my_dict['машина'] = ", my_dict['машина'])
a = my_dict.get('кот', 'Мурзик')    # найти ключ 'кот', а если его нет - вернуть 'Мурзик'
print(a)
a = my_dict.get('слон', 'Джумбо')
print(a)
my_dict.setdefault('кот', 'Мурзик')  # если не найден - добавить ключ "кот" и значение "Мурзик"
print(my_dict)

my_dict = {'один': 'one', 'два': 'two'}
print(my_dict)
a = 'один' in my_dict
print("'один' in my_dict:", a)
a = 'one' in my_dict
print("'one' in my_dict:", a)


print('------ Множества --------')

my_set = set()
print(my_set)
my_set = {1, 2, 3, 4, 4, 5, 6, 5, 6, 99}
print(my_set)
other_set = {1, 3, 5, 21}
print(other_set)
a = my_set | other_set  # объединение 2-х множеств
print(a)
a = my_set & other_set  # пересечение 2-х множеств
print(a)
a = my_set - other_set  # уникальные значения из множества my_set
print(a)
a = other_set - my_set  # уникальные значения из множества other_set
print(a)


print('------ Работа с файлами --------')

print(ord('h'))     # символ в код
print(chr(104))     # код в символ
print(hex(104))     # 16-ричное представление кода

print('\n')

for code in range(128):
    print(code, hex(code), chr(code))

print('\n')

bb = b'\xd1\x86'
bn = '\xd1\x86'
print(bb)
print(bn)

print('\n')

bb = b'\xd0\xbf\xd1\x80\xd0\xd8\xb2\xd0\xb5\xd1\x82'
print(bb)
print(type(bb))
print(hex(bb[0]))
print(bb[0])
print(bb.count(0xd0))
print(b'he' + b'llo')

# bb[1] = hex(20)     # ошибка: последовательность байт - неизменяемая

print('\n')

print(bin(0xd1))
print(bin(0x84))

code = 0b10001000100
print(code, hex(code), chr(code))

print('\n')

ba = bytearray(b'hello')
ba[0] = 32      # код пробела
print(ba)

print('\n')

print('привет'.encode(encoding='utf-8'))
print('привет'.encode(encoding='utf-16'))
print('привет'.encode(encoding='cp866'))

print(b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode('utf-8'))
