from microbit import *

import speech
import random

image_list = [Image.HAPPY,
              Image.SAD,
              Image.YES,
              Image.NO,
              Image.HEART,
              Image.SMILE,
              Image.CONFUSED,
              Image.ANGRY,
              Image.ASLEEP,
              Image.SURPRISED,
              Image.SILLY,
              Image.FABULOUS,
              Image.MEH]

for p in [20, 50, 100]:
    for name in ['Alison', 'Madi', 'Milli', 'Isaac', 'Tim', 'Harley']:
        display.show(random.choice(image_list))
        speech.say('hello '+name, pitch=p, speed=100)
        sleep(1000)
