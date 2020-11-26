from numpy.core.numeric import load
import pyautogui
from PIL import Image
import pytesseract
import time


class ComputerEyes:

    def __init__(self):
        self.shopText = []
        self.subshots = []
        self.image = Image

    def takeScreenshot(self):
        self.image = Image.open("screenshot.png")
        time.sleep(2)

    def createSubshots(self):
        i = 0
        left = 483
        top = 1044
        right = 630
        bottom = 1066
        sc = self.image
        while i < 5:
            cropped = sc.crop(
                (left + 200*i, top, right + 200*i, bottom))
            self.subshots.append(cropped)
            cropped.show()
            i = i+1

    def processSubshots(self):
        i = 0
        while i < 5:
            self.shopText.append(pytesseract.image_to_string(self.subshots[i]))
            print(i, self.shopText[i])
            i = i+1

    def refresh(self):
        self.takeScreenshot()
        self.createSubshots()
        self.processSubshots()

    def getSubshots(self):
        self.refresh()
        return self.subshots

    # crops image and returns true if it is planning phase
    def checkForRoundStart(self):
        left = 775
        top = 123
        right = 1130
        bottom = 220
        sc = self.image.crop(left, top, right, bottom)
        if pytesseract.image_to_string(sc) == "Planning":
            return True
        return False
