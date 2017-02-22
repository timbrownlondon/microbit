from microbit import *


def brighten(x, y):
    if(display.get_pixel(x, y) < 9):
        display.set_pixel(x, y, display.get_pixel(x, y) + 1)


x = 2
y = 2
while True:
    brighten(x, y)
    sleep(200)

    if accelerometer.get_x() > 25 and x < 4:
        x += 1
    elif accelerometer.get_x() < -25 and x > 0:
        x -= 1

    if accelerometer.get_y() > 25 and y < 4:
        y += 1
    elif accelerometer.get_y() < -25 and y > 0:
        y -= 1
