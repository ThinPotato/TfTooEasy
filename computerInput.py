import pyautogui


class ComputerInput:

    def __init__(self):
        self.buyX = 400
        self.buyY = 1000
        self.benchX = 550
        self.benchY = 800

    def buyCharacter(self, location=0):
        if location == 0:
            pyautogui.moveTo(self.buyX, self.self.buyY)
        elif location == 1:
            pyautogui.moveTo(self.buyX * 2, self.buyY)
        elif location == 2:
            pyautogui.moveTo(self.buyX * 3, self.buyY)
        elif location == 3:
            pyautogui.moveTo(self.buyX * 4, self.buyY)
        elif location == 4:
            pyautogui.moveTo(self.buyX * 5, self.buyY)
        pyautogui.click

    def refreshStore():
        pyautogui.press("d")

    def buyExp():
        pyautogui.press("f")

    def sellCharacterFrombench(self, benchLocation=0):
        pyautogui.moveTo(self.benchX * benchLocation + 1, self.benchY)
        pyautogui.click
        pyautogui.moveTo(1000, 1070)
        pyautogui.click

    def benchToMap(self, benchLocation, mapX, mapY):
        position = self.mapPositionResolver(mapX, mapY)
        pyautogui.moveTo(self.benchX * benchLocation + 1, self.benchY)
        pyautogui.click
        pyautogui.moveTo(position[0], position[1])
        pyautogui.click

    def mapPositionResolver(self, x, y):
        finalX = -1
        finalY = -1
        leftX = 560
        rightX = 610
        boardY = 455
        if y % 2 == 0:
            finalX = leftX * x
            finalY = boardY * y
        else:
            finalX = rightX * x
            finalY = boardY * y
        return [finalX, finalY]
