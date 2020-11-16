
import simple_draw as sd

CONST_POWER_OF_GRAVITY = 20
CONST_MAX_POWER_OF_WIND = 10
CONST_SLEEP_TIME = 0.02


def random_snowflake_length(start, end):
    return sd.randint(start, end)


def power_of_wind(start, end):
    return sd.randint(start, end)


def snowflakes_down_draw(x, y, length, color):
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=length, color=color)


# def snowflakes_down(x, y, length):
def snowflakes_down(snowflakes_coords):
    while True:
        # sd.clear_screen()

        i = 0
        reset_i = 0
        finish_snowflakes = 0

        while i < len(snowflakes_coords):
            if i == reset_i:
                i = finish_snowflakes
                reset_i += 1

            x, y, length = snowflakes_coords[i][0], snowflakes_coords[i][1], snowflakes_coords[i][2]

            if y < length:
                if finish_snowflakes < i:
                    finish_snowflakes += 1
                i += 1
                continue

            sd.start_drawing()  # Всё, что рисуется далее, будет выведено на экран во время sd.finish_drawing()

            snowflakes_down_draw(x=x, y=y, length=length, color=sd.background_color)

            y -= CONST_POWER_OF_GRAVITY     # снизили высоту снежинки
            x = x + power_of_wind(-CONST_MAX_POWER_OF_WIND, CONST_MAX_POWER_OF_WIND)    # сдвинули влево/вправо (ветер)
            snowflakes_coords[i] = [x, y, length]   # записали новые координаты снежинки, чтобы потом "стереть"

            snowflakes_down_draw(x=x, y=y, length=length, color=sd.COLOR_WHITE)

            sd.finish_drawing()  # Всё, что рисовали, начиная с sd.start_drawing(), будет выведено на экран здесь.

            sd.sleep(CONST_SLEEP_TIME/(i+1-finish_snowflakes))

            i += 1

        if y < length:
            break

        if sd.user_want_exit():
            break
