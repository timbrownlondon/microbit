from microbit import *

# attach piezo buzzer between GRD and Pin0
val = 5

while True:
    for i in range(200):
        pin0.write_digital(1)
        sleep(val)
        pin0.write_digital(0)
        sleep(val)
    if button_a.is_pressed() and val < 9:
        val += 1
        display.show(str(val))
    elif button_a.is_pressed() and val > 1:
        val -= 1
        display.show(str(val))
    sleep(1000)
