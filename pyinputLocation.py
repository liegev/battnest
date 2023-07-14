import time
from pynput.mouse import Controller

mouse = Controller()

while True:
    print('The current pointer position is {0}'.format(mouse.position))
    time.sleep(1)  # Delay for 1 second
