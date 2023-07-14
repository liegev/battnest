#! /usr/bin/env python3

import pytesseract
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
    """ Given a rectangle, return a PIL Image of that part of the screen.
        Handles a Linux installation with an older Pillow by falling-back
        to using XLib """
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

# Specify the screen region here
x = 1488
y = 338
width = 1549 - x
height = 377 - y

# Area of screen to monitor
screen_rect = [x, y, width, height]  

## print("Watching: " + str(screen_rect))

### Loop forever, monitoring the user-specified rectangle of the screen
while True: 
    image = screenGrab(screen_rect)              # Grab the area of the screen
    text  = pytesseract.image_to_string(image)   # OCR the image

    # IF the OCR found anything, write it to stdout.
    text = text.strip()
    #if len(text) > 0:
    print(text)
    

    text = text.replace("%", "")

    # convert the string to an integer
    text = int(text)

    # check if value of the variable 'text' is less than 60
    if text > 90:
        subprocess.run(["python", "clickhere60.py"])

    if text < 80:
        subprocess.run(["python", "clickhere77.py"])

