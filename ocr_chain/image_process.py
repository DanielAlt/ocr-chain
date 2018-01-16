# import the necessary packages
from .core import (helpers, logger)

import threading, os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

class ImageProcess(threading.Thread):

    def __init__(self, filepath, output_dir):
        threading.Thread.__init__(self)
        self.filepath = filepath
        self.output_dir = output_dir

    def run(self):
        """ load the image as a PIL/Pillow image, apply OCR """
        text = pytesseract.image_to_string(Image.open(self.filepath))

        """ Write Output to a Test File """
        output_path = os.path.join(self.output_dir, os.path.split(self.filepath)[-1]+".txt")
        with open(output_path, 'wb') as f:
            f.write(str(text).encode("utf8"))
            f.close()
