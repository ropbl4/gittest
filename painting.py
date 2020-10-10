import random
import simple_draw as sd

sd.resolution = (1300, 800)  # разрешение полотна

point = sd.get_point(100, 100)  # точка на полотне (x, y)
radius = 50

for _ in range(3):
    sd.circle(center_position=point, radius=radius)  # рисуем круг с центром в точке center_position и радиусом radius
    radius += 5


def bubble(point, step):
    radius = 50
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, width=2)    # тут ещё ширина линии width пикселей
        radius += step


for i in range(100, 1001, 100):
    for j in range(400, 601, 100):
        point = sd.get_point(i, j)
        bubble(point=point, step=10)

for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point, step)

sd.pause()
