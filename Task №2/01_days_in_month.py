# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

# TODO здесь ваш код
number_of_days = 0

if month == 1:
    number_of_days = 31
elif month == 2:
    number_of_days = 28
elif month == 3:
    number_of_days = 31
elif month == 4:
    number_of_days = 30
elif month == 5:
    number_of_days = 31
elif month == 6:
    number_of_days = 30
elif month == 7:
    number_of_days = 31
elif month == 8:
    number_of_days = 31
elif month == 9:
    number_of_days = 30
elif month == 10:
    number_of_days = 31
elif month == 11:
    number_of_days = 30
elif month == 12:
    number_of_days = 31
else:
    print("это некорректный номер !")

if 1 <= month <= 12:
    print(number_of_days, 'дней.')
