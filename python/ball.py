from microbit import *

import random


class Ball:

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dy = dx
        self.dx = dy

    def move(self):
        display.set_pixel(self.x, self.y, 0)
        self.y += self.dy
        self.x += self.dx

        if(self.y == 0):
            self.dy = 1
            self.dx = random.choice([-1, 0, 1])
        if(self.y == 4):
            self.dy = -1
            self.dx = random.choice([-1, 0, 1])

        if(self.x == 0):
            self.dx = 1
        if(self.x == 4):
            self.dx = -1

    def show(self):
        display.set_pixel(self.x, self.y, 5)


class Player:

    def __init__(self, x):
        self.x = x

    def move(self, direction):
        display.set_pixel(self.x, 4, 0)
        self.x += direction
        if(self.x < 0):
            self.x = 0
        if(self.x > 4):
            self.x = 4

    def show(self):
        display.set_pixel(self.x, 4, 5)


player = Player(2)
ball = Ball(2, 1, 1, 1)

while(True):
    player.show()
    ball.show()

    sleep(300)

    ball.move()
    if button_a.was_pressed():
        player.move(-1)
    if button_b.was_pressed():
        player.move(1)
