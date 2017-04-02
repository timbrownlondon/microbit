from microbit import *
import radio
import random

# setup
radio.on()
moves = ['R', 'P', 'S']
choice = random.randint(0, 2)
my_score = 0
others_score = 0


def get_others_move():
    while(True):
        message = radio.receive()
        if message in moves:
            display.show(Image.CHESSBOARD)
            sleep(1000)
            return message


def first_player_won(my_choice, their_choice):
    if my_choice == 'R' and their_choice == 'S':
        return True
    if my_choice == 'P' and their_choice == 'R':
        return True
    if my_choice == 'S' and their_choice == 'P':
        return True
    return False


def show_scores():
    scores = str(my_score) + '-' + str(others_score) + ' '
    display.scroll(scores, delay=200)


display.scroll('***')
while True:
    if button_a.was_pressed():
        choice = (choice + 1) % len(moves)
    display.show(moves[choice])
    sleep(100)
    if button_b.was_pressed():
        display.show(Image.ARROW_N)
        radio.send(moves[choice])
        sleep(200)

        others_move = get_others_move()

        display.scroll(moves[choice] + '-' + others_move)

        if first_player_won(moves[choice], others_move):
            display.show(Image.HAPPY)
            my_score += 1
        elif first_player_won(others_move, moves[choice]):
            display.show(Image.SAD)
            others_score += 1
        else:
            display.show('-')
        sleep(1000)

        while not button_a.was_pressed():
            sleep(50)
        show_scores()
        display.scroll('***')

        # clear any presses ready for next turn
        button_a.get_presses()
        button_b.get_presses()
        choice = random.randint(0, 2)


