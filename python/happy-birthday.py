from microbit import *
import random
import music

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
        sleep(700)
        display.show(' ')
        sleep(100)

music.set_tempo(bpm=300)

while True:
    display.show(Image.HEART)
    sleep(3000)
    music.play(music.BIRTHDAY, wait=False)
    show_text('HAPPYBIRTHDAY')
    display.show(' ', 300)
    show_animation(random.choice(invaders))
