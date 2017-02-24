from microbit import *
import music

while True:
    for pitch in range(1000, 200, -100):
        music.pitch(pitch, 500, wait=True)
    sleep(1000)
