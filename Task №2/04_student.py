# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код
percent = 3
percent_in_rub = expenses / 100 * percent
expenses_plus_percent = expenses
i = 0
result = 0


while i < 10:
    result += expenses + percent_in_rub * i - educational_grant
    i += 1

print(f'Студенту надо попросить {result} рублей')

# 12 000 * 10 = 120 000 - 10 мес без %
# со 2-го по 10-й мес. (9 раз) прибавляем 3% от 12 000 (т.е. 360 руб) = 3 240
# итоговые траты = 123 240, вычтем 100 000, не хватает 23 240
