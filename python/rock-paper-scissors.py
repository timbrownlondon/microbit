from microbit import *


def read_buttons():
    a = button_a.was_pressed()
    b = button_b.was_pressed()
    # scissors
    if a and b:
        return('S')
    # rock
    if a:
        return('R')
    # paper
    if b:
        return('P')
    return ' '


def count_down():
    for n in ['3', '2', '1', '0']:
        display.show(n)
        sleep(1000)


while(True):
    count_down()
    my_go = read_buttons()
    display.show(my_go)
    sleep(3000)
