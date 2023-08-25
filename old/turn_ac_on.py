from pynput.mouse import Button, Controller

mouse = Controller()

# Move the pointer to the specific location (e.g., (100, 200))
mouse.position = (2518, 530)

# Click the left button
mouse.click(Button.left, 1)
