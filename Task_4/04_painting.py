# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# TODO здесь ваш код
import Task_4.paint_pack.draw_primitives as dp
import Task_4.paint_pack.draw_smile as dsm
import Task_4.paint_pack.draw_snow as dsn

dp.sd.resolution = (1920, 1010)

dp.rainbow(x=900, y=700, start_radius=150, width=20)
dp.wall(x_start=550, y_start=5, brick_width=100, brick_height=50, bricks_num_width=7, bricks_num_height=7)
dp.tree(x=1640, y=5, length=150)
dsm.smile(x=900, y=205, color=dp.sd.COLOR_YELLOW)

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

snowflakes_coords = []

for _ in range(50):
    snowflake_length = dsn.random_snowflake_length(10, 20)
    x_start = dsn.sd.random_number(0 + snowflake_length, 400 - snowflake_length)
    y_start = dsn.sd.resolution[1] - snowflake_length

    snowflakes_coords.append([x_start, y_start, snowflake_length])

dsn.snowflakes_down(snowflakes_coords)

dp.pause()
