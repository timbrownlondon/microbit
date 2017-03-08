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

        if(self.x == 0):
            self.dx = 1
            self.dy = random.choice([-1, 0, 1])
        if(self.x == 4):
            self.dx = -1
            self.dy = random.choice([-1, 0, 1])

        if(self.y == 0):
            self.dy = 1
        if(self.y == 4):
            self.dy = -1

    def show(self):
        display.set_pixel(self.x, self.y, 9)


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 1

    def move(self):
        display.set_pixel(self.x, self.y, 0)
        self.y += self.direction
        if(self.y == 0):
            self.direction = 1
        if(self.y == 4):
            self.direction = -1

    def show(self):
        display.set_pixel(self.x, self.y, 5)


player_a = Player(0, 2)
player_b = Player(4, 2)
ball = Ball(2, 1, 1, 1)

while(True):
    player_a.show()
    player_b.show()
    ball.show()

    sleep(200)

    ball.move()
    if button_a.was_pressed():
        player_a.move()
    if button_b.was_pressed():
        player_b.move()
