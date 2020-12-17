zoo_pet_mass = {
    'lion': 300,
    'skunk': 5,
    'elephant': 5000,
    'horse': 400
}

d1 = {"Russia": "Moscow", "USA": "Washington"}
print(d1)
d1["China"] = "Beijing"
print(d1)
# {'Russia': 'Moscow', 'China': 'Beijing', 'USA': 'Washington'}

del d1["China"]
print(d1)
# {'Russia': 'Moscow', 'USA': 'Washington'}


value_search = 300

key = list(zoo_pet_mass.keys())[list(zoo_pet_mass.values()).index(value_search)]     # Ключ, зная значение
print(f'\nКлюч: {key}\n')

zoo_values_dict = zoo_pet_mass.values()     # Ключ, зная значение (более подробно) - Start
zoo_values_list = list(zoo_values_dict)
zoo_index = zoo_values_list.index(value_search)
zoo_keys = zoo_pet_mass.keys()
zoo_keys_list = list(zoo_keys)
key = zoo_keys_list[zoo_index]

print(f'zoo_values_dict: {zoo_values_dict}')
print(f'zoo_values_list: {zoo_values_list}')
print(f'zoo_index: {zoo_index}')
print(f'zoo_keys: {zoo_keys}')
print(f'zoo_keys_list: {zoo_keys_list}')
print(f'Ключ: {key}\n')                     # Ключ, зная значение (более подробно) - End

for key, value in zoo_pet_mass.items():
    if value == value_search:
        print(f'Ключ: {key}')

print('\n-----------------------------\n')

value = zoo_pet_mass['lion']    # Значение, зная ключ
print(f'Значение: {value}')

print('\n-----------------------------\n')

for key in zoo_pet_mass:  # ключи в цикле
    print(f'Ключ: {key}')

print('\n-----------------------------\n')

for value in zoo_pet_mass.values():  # значения в цикле
    print(f'Значение: {value}')


print('\n-----------------------------\n')

for key, value in zoo_pet_mass.items():  # ключи и значения в цикле
    print(f'Ключ: {key}, значение: {value}')
