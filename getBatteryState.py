import pytesseract
from PIL import Image

def get_text_from_image(x, y, width, height):
    try:
        image = ImageGrab.grab(bbox=[x, y, x+width, y+height])
    except ImportError:
        dsp = display.Display()
        root = dsp.screen().root
        raw_image = root.get_image(x, y, width, height, X.ZPixmap, 0xffffffff)
        image = Image.frombuffer("RGB", (width, height), raw_image.data, "raw", "BGRX", 0, 1)

    text = pytesseract.image_to_string(image)
    return text.strip()

if __name__ == "__main__":
    x = 969
    y = 318
    width = 1029 - x
    height = 353 - y

    text = get_text_from_image(x, y, width, height)
    print(text)
