import pyautogui
from PIL import Image
import pytesseract


class ComputerEyes:

    def __init__(self):
        self.shopText = ["", "", "", "", ""]
        self.subshots = [None, None, None, None, None]
        self.image

    def takeScreenshot(self):
        self.image = pyautogui.screenshot('screenshot.png')

    def createSubshots(self):
        left = 490
        top = 990
        right = 690
        bottom = 1070
        sc = Image.open("screenshot.png")
        for x in self.subshots:
            self.subshots[x] = sc.crop(
                left * (x+1), top, right * (x+1), bottom)

    def processSubshots(self):
        for x in self.shopText:
            self.shopText[x] = pytesseract.image_to_string(self.subshots[x])

    def refresh(self):
        self.takeScreenshot
        self.createSubshots
        self.processSubshots

    def getSubshots(self):
        self.refresh
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
