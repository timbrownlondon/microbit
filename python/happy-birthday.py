from microbit import *
import random

invaders = [
    [
        Image("09990:90909:99999:90009:09090"),
        Image("09990:90909:99999:90009:90009")
    ],
    [
        Image("00900:09990:99999:90009:09090"),
        Image("00900:09990:99999:09090:90009")
    ],
    [
        Image("09990:90909:99999:90009:09090"),
        Image("09990:90909:99999:09090:90009")
    ]
]

def show_animation(image_list):
    for _ in range(8):
        display.show(image_list, delay=500)
    display.show('')
    sleep(500)

def show_text(text):
    for char in text:
        display.show(char)
        sleep(1000)
        display.show(' ')
        sleep(100)

while True:
    display.show(Image.HEART)
    sleep(3000)
    show_text('HAPPYBIRTHDAY')
    display.show(Image.HEART)
    sleep(3000)
    show_animation(random.choice(invaders))
