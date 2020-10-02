zoo_pet_mass = {
    'lion': 300,
    'skunk': 5,
    'elephant': 5000,
    'horse': 400
}

total_mass = 0

for animal, mass in zoo_pet_mass.items():  # выдаём ключ и значение
    print(animal, mass)
    total_mass += mass

print('Общая масса животных:', total_mass)

for animal in zoo_pet_mass:  # выдаём только ключ
    print(animal)

for mass in zoo_pet_mass.values():  # выдаём только значение
    print(mass)
    total_mass += mass


def multiply(param_1, param_2):
    print('Функцию вызвали с параметрами:', param_1, 'и', param_2)
    if isinstance(param_1, int) and isinstance(param_2, int):
        value = param_1 ** param_2
        return value
    return 'error'


print(multiply(2, 3))
print(multiply('привет!', 5))


def change_param(param_1):
    param_1 *= 2
    return param_1


a = 3
print(change_param(a))
print('a =', a)


def change_list(param_1):
    param_1 = param_1.remove('one')
    return param_1


a_list = ['one', 'two']
print(change_list(a_list))
print('a =', a_list)
