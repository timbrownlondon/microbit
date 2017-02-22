from microbit import *

import random

dice_face = [
    Image('::009'),
    Image(':09::0009'),
    Image(':09:009:0009'),
    Image(':0909::0909'),
    Image(':0909:009:0909'),
    Image(':0909:0909:0909')
]


def throw_dice():
    for i in range(10):
        for n in range(6):
            display.show(dice_face[n])
            sleep(40)


outcome = random.choice(range(6))
while(True):
    if button_a.is_pressed():
        throw_dice()
        outcome = random.choice(range(6))
    sleep(50)
    display.show(dice_face[outcome])
    if button_b.is_pressed():
        display.show(str(outcome + 1))

    
    
