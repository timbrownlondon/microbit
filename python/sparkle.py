from microbit import *

import random

while(True):
    sleep(500)
    for x in range(0, 5):
        for y in range(0, 5):
            display.set_pixel(x, y, random.choice(range(1, 10)))
