import simple_draw as sd

# sd.resolution = (1600, 1000)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def pause():
    sd.pause()


def rectangle(left_bottom_x, left_bottom_y, right_top_x, right_top_y, contour=False, contour_color=sd.COLOR_ORANGE):
    left_bottom_point = sd.get_point(left_bottom_x, left_bottom_y)
    right_top_point = sd.get_point(right_top_x, right_top_y)

    sd.rectangle(left_bottom=left_bottom_point, right_top=right_top_point, color=sd.background_color, width=0)

    if contour:
        sd.rectangle(left_bottom=left_bottom_point, right_top=right_top_point, color=contour_color, width=3)


def rainbow(x, y, start_radius=50, width=4):
    point = sd.get_point(x, y)

    count = 0

    for _ in range(10):
        count += 1

        if count >= len(rainbow_colors):
            count -= len(rainbow_colors)

        sd.start_drawing()

        for i in range(len(rainbow_colors)):
            shift = count + i

            if shift >= len(rainbow_colors):
                shift -= len(rainbow_colors)

            radius = start_radius + (width + 1) * i
            sd.circle(center_position=point, radius=radius, color=rainbow_colors[shift], width=width)

        sd.finish_drawing()

        sd.sleep(0.5)

    rectangle(point.x - radius, point.y - radius, point.x + radius, point.y)

    # sd.pause()


def wall(x_start=50, y_start=50, brick_width=100, brick_height=50, bricks_num_width=7, bricks_num_height=7):
    x_end = x_start + brick_width
    y_end = y_start + brick_height

    for i in range(bricks_num_width):
        for j in range(bricks_num_height):
            if j % 2 == 0:
                point_start = sd.get_point(x_start + i * brick_width, y_start + j * brick_height)
                point_end = sd.get_point(x_end + i * brick_width, y_end + j * brick_height)
            else:
                point_start = sd.get_point(x_start + i * brick_width + brick_width / 2, y_start + j * brick_height)
                point_end = sd.get_point(x_end + i * brick_width + brick_width / 2, y_end + j * brick_height)

            sd.rectangle(left_bottom=point_start, right_top=point_end, color=sd.COLOR_ORANGE, width=4)

    # Крыша
    sd.line(start_point=sd.get_point(x_start-100, y_start+305), end_point=sd.get_point(x_start+350, y_start+505), color=sd.COLOR_ORANGE, width=5)
    sd.line(start_point=sd.get_point(x_start+350, y_start+505), end_point=sd.get_point(x_start+800, y_start+305), color=sd.COLOR_ORANGE, width=5)

    # Окно
    rectangle(left_bottom_x=x_start+230, left_bottom_y=y_start+75, right_top_x=x_start+470, right_top_y=y_start+315, contour=True)


def tree(x=300, y=5, length=150):
    def branch(point, angle, length, delta):
        if length < 1:
            return
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        next_point = v1.end_point
        next_angle = angle - delta
        next_length = length * .75
        branch(point=next_point, angle=next_angle, length=next_length, delta=delta)

    point_0 = sd.get_point(x, y)

    for delta in range(-50, 51, 10):
        branch(point=point_0, angle=90, length=length, delta=delta)
