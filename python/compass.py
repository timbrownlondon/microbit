from microbit import *

compass.calibrate()

while True:
    needle = ((15 - compass.heading()) // 30) % 12
    display.scroll(str(needle))
    display.show(Image.ALL_CLOCKS[needle])
    sleep(700)
