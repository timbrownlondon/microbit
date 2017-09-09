from microbit import *
# import music

n = 0
x = 0
y = 0
z = 0
delta = 150
pitch = 1760
mode_on = False


def pix(n):
    i = n % 25
    brightness = (((n // 25) + 1) % 2) * 5
    display.set_pixel(i % 5, i // 5, brightness)


def check(x, y, z):
    detected = False
    xa = accelerometer.get_x()
    ya = accelerometer.get_y()
    za = accelerometer.get_z()

    if abs(x - xa) > delta or abs(y - ya) > delta or abs(z - za) > delta:
        detected = True
    return (detected, xa, ya, za)


while(True):
    pix(n)
    sleep(800)
    if button_a.was_pressed():
        mode_on = not mode_on
        if mode_on:
            display.show('+')
        if not mode_on:
            display.show('-')
        sleep(500)
        display.clear()
    if button_b.was_pressed():
        display.scroll(str(n))
    (moved, x, y, z) = check(x, y, z)
    if mode_on and moved:  # or button_a.was_pressed():
        n += 1
        # music.pitch(int(pitch), 80)
