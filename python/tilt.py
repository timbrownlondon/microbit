from microbit import *

x = 2
y = 2
while True:
    display.set_pixel(x, y, 9)
    sleep(300)
    display.clear()

    if accelerometer.get_x() > 25 and x < 4:
        x += 1
    elif accelerometer.get_x() < -25 and x > 0:
        x -= 1

    if accelerometer.get_y() > 25 and y < 4:
        y += 1
    elif accelerometer.get_y() < -25 and y > 0:
        y -= 1
