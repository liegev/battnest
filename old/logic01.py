#! /usr/bin/env python3

import pytesseract
import subprocess
import time
import datetime
from PIL import Image


def turn_off_ac():
    print("battery state fell below 85. Turning AC off...")
    subprocess.run(["python", "turn_ac_off.py"])

def turn_on_ac():
    print("battery state rose above 98. Turning AC on...")
    subprocess.run(["python", "turn_ac_on.py"])

# Import ImageGrab if possible, might fail on Linux
try:
    from PIL import ImageGrab
    use_grab = True
except ImportError:
    # Some older versions of pillow don't support ImageGrab on Linux
    # In which case we will use XLib 
    from Xlib import display, X   
    use_grab = False

def screenGrab(rect):
    global use_grab
    x, y, width, height = rect

    if use_grab:
        image = ImageGrab.grab(bbox=[x, y, x+width, y+height])
    else:
        # ImageGrab can be missing under Linux
        dsp = display.Display()
        root = dsp.screen().root
        raw_image = root.get_image(x, y, width, height, X.ZPixmap, 0xffffffff)
        image = Image.frombuffer("RGB", (width, height), raw_image.data, "raw", "BGRX", 0, 1)
    return image


x = 969
y = 318
width = 1029 - x
height = 353 - y
screen_rect = [x, y, width, height]  

ac_on = False

while True: 
    image = screenGrab(screen_rect)
    text  = pytesseract.image_to_string(image)
    text = text.strip()
    text = text.replace("%", "")
    batState = int(text)
    print(f"Current battery state: {batState}")

    if batState > 95 and not ac_on:
        turn_on_ac()
        ac_on = True
    elif batState <= 90 and ac_on:
        turn_off_ac()
        ac_on = False

    current_time = datetime.datetime.now()
    print("Current time:", current_time)
    print("AC on =",ac_on)
    time.sleep(60*5)  # Wait for 1 second before checking again
