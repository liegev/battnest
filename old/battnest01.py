#! /usr/bin/env python3

import pytesseract
import subprocess
from PIL import Image

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

last_state_90 = False
last_state_80 = False

while True: 
    image = screenGrab(screen_rect)
    text  = pytesseract.image_to_string(image)
    text = text.strip()
    text = text.replace("%", "")
    print('raw thing is',text)
    batState = int(text)
    print(batState)