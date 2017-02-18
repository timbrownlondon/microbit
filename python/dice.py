from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        display.show('?')
        sleep(700)
        display.show(random.choice(['1', '2', '3', '4', '5', '6']))
