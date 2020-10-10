# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры hole_x, hole_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

hole_x, hole_y = 10, 7
paper_x, paper_y = 8, 9


# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

# TODO здесь ваш код
def check_paper_in_hole(hole_x, hole_y, paper_x, paper_y):
    result_string_start = 'e_x =' + str(hole_x) + ', e_y =' + str(hole_y) + ', p_x =' + str(paper_x), ' + p_y =' + str(paper_y)
    if (paper_x <= hole_x and paper_y <= hole_y) or (paper_y <= hole_x and paper_x <= hole_y):
        print(result_string_start, ' -> уместится !')
    else:
        print(result_string_start, ' -> не влезает !')


check_paper_in_hole(10, 7, 8, 9)
check_paper_in_hole(10, 7, 9, 8)
check_paper_in_hole(10, 7, 6, 8)
check_paper_in_hole(10, 7, 8, 6)
check_paper_in_hole(10, 7, 3, 4)
check_paper_in_hole(10, 7, 11, 9)
check_paper_in_hole(10, 7, 9, 11)

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

# hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)

print('\n=========================\n')


# TODO здесь ваш код
def check_brick_in_hole(brick_x, brick_y, brick_z, hole_x=8, hole_y=9):
    result_string_start = 'h_x =' + str(hole_x) + ', h_y =' + str(hole_y) + ', b_x =' + \
                          str(brick_x) + ', b_y =' + str(brick_y) + ', b_z =' + str(brick_z)
    result_string_end_yes = ' -> уместится !'
    result_string_end_no = ' -> не влезает !'

    if (brick_x <= hole_x and brick_y <= hole_y) or (brick_y <= hole_x and brick_x <= hole_y):
        print(result_string_start, result_string_end_yes)
    elif (brick_x <= hole_x and brick_z <= hole_y) or (brick_z <= hole_x and brick_x <= hole_y):
        print(result_string_start, result_string_end_yes)
    elif (brick_z <= hole_x and brick_y <= hole_y) or (brick_y <= hole_x and brick_z <= hole_y):
        print(result_string_start, result_string_end_yes)
    else:
        print(result_string_start, result_string_end_no)


check_brick_in_hole(11, 10, 2)
check_brick_in_hole(11, 2, 10)
check_brick_in_hole(10, 11, 2)
check_brick_in_hole(10, 2, 11)
check_brick_in_hole(2, 10, 11)
check_brick_in_hole(2, 11, 10)
check_brick_in_hole(3, 5, 6)
check_brick_in_hole(3, 6, 5)
check_brick_in_hole(6, 3, 5)
check_brick_in_hole(6, 5, 3)
check_brick_in_hole(5, 6, 3)
check_brick_in_hole(5, 3, 6)
check_brick_in_hole(11, 3, 6)
check_brick_in_hole(11, 6, 3)
check_brick_in_hole(6, 11, 3)
check_brick_in_hole(6, 3, 11)
check_brick_in_hole(3, 6, 11)
