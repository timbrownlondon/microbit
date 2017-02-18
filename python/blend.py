from microbit import *

for x in range(0, 5):
    for y in range(0, 5):
        display.set_pixel(x, y, x+y % 9 + 1)

while(True):
    sleep(500)
    while button_a.is_pressed():
        sleep(100)
    for x in range(0, 5):
        for y in range(0, 5):
            display.set_pixel(x, y, display.get_pixel(x, y) % 9 + 1)
