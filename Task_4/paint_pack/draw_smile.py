
import simple_draw as sd


def smile(x, y, color):
    width = 2
    shift_eye_x = 60
    shift_eye_y = 20
    shift_eye_up_x = 10
    shift_eye_up_y = 10
    shift_mouth_y = 20
    radius = 100

    # Head
    sd.circle(center_position=sd.get_point(x, y), radius=radius, color=color, width=width)

    # Left eye
    point_start = sd.get_point(x - shift_eye_x, y + shift_eye_y)
    point_end = sd.get_point(x - shift_eye_x + shift_eye_up_x, y + shift_eye_y + shift_eye_up_y)
    sd.line(point_start, point_end, color=color, width=width)

    point_start = sd.get_point(x - shift_eye_x + shift_eye_up_x, y + shift_eye_y + shift_eye_up_y)
    point_end = sd.get_point(x - shift_eye_x + shift_eye_up_x * 2, y + shift_eye_y)
    sd.line(point_start, point_end, color=color, width=width)

    # Right eye
    point_start = sd.get_point(x + shift_eye_x, y + shift_eye_y)
    point_end = sd.get_point(x + shift_eye_x - shift_eye_up_x, y + shift_eye_y + shift_eye_up_y)
    sd.line(point_start, point_end, color=color, width=width)

    point_start = sd.get_point(x + shift_eye_x - shift_eye_up_x, y + shift_eye_y + shift_eye_up_y)
    point_end = sd.get_point(x + shift_eye_x - shift_eye_up_x * 2, y + shift_eye_y)
    sd.line(point_start, point_end, color=color, width=width)

    # Mouth
    point_start = sd.get_point(x - shift_eye_x + shift_eye_up_x * 3, y - shift_mouth_y)
    point_end = sd.get_point(x + shift_eye_x - shift_eye_up_x * 3, y - shift_mouth_y)
    sd.line(point_start, point_end, color=color, width=width)
