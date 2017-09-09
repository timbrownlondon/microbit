from microbit import *
import music

pitch = 440
interval = 1.12245
while True:
    if button_a.was_pressed():
        pitch *= interval
        music.pitch(int(pitch), 300)
    if button_b.was_pressed():
        pitch /= interval
        music.pitch(int(pitch), 300)
