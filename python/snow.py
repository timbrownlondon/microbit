from microbit import *

import random

picture = Image("00000:00000:00000:00000:00000")

while(True):
    sleep(700)
    picture = picture.shift_down(1)
    picture.set_pixel(random.randrange(5), 0, random.randrange(10))
    display.show(picture)
