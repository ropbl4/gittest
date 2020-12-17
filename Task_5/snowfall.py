import simple_draw as sd

snowflakes_coords = []


def create_snowflake(n):     # создает N снежинок
    for i in range(n):
        snowflake_length = sd.randint(5, 15)
        snowflake_x = sd.random_number(0 + snowflake_length, sd.resolution[0] - snowflake_length)
        snowflake_y = sd.resolution[1] - snowflake_length

        snowflakes_coords.append([snowflake_x, snowflake_y, snowflake_length])


def paint_all_snowflakes_with_color(color):   # отрисовывает все снежинки цветом color
    for i in range(len(snowflakes_coords)):
        point = sd.get_point(snowflakes_coords[i][0], snowflakes_coords[i][1])
        sd.snowflake(center=point, length=snowflakes_coords[i][2], color=color)


def move_snowflakes():    # сдвигает снежинки на один шаг
    for i in range(len(snowflakes_coords)):
        snowflakes_coords[i][1] -= snowflakes_coords[i][2]


def numbers_of_snowflakes_out_of_screen():   # выдает список номеров снежинок, которые вышли за границу экрана
    numbers_out_of_screen = []

    for i in range(len(snowflakes_coords)):
        if snowflakes_coords[i][1] < 0:
            numbers_out_of_screen.append(i)

    return numbers_out_of_screen


def remove_snowflakes(numbers):   # удаляет снежинки с номерами из списка
    for i in numbers[::-1]:
        # point = sd.get_point(snowflakes_coords[i][0], snowflakes_coords[i][1])
        # sd.snowflake(center=point, length=snowflakes_coords[i][2], color=sd.background_color)
        snowflakes_coords.pop(i)

