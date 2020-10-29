from character import Character
from computerInput import ComputerInput
import character
from computerEyes import ComputerEyes
from virtualBoard import VirtualBoard
from collections import defaultdict
from computerInput import ComputerInput


class Build:

    def __init__(self):
        # List of characters that are already at max level
        self.goldList = []

        # Characters nearly complete : priority + 2
        # native priority if is included : priority 1
        # desiredCharacters list is sorted based upon inherent priority.
        self.priorityList = defaultdict(int)
        self.characterCountList = defaultdict(int)

    # Turn playbook:
    # 1. Buy characters
    # 2. Place characters
    # 3. Collect items
    # 4. Place items
    # 5. buy Exp (if on turn xth turn)
    def playTurn():
        pass

    # Buy Playbook:
    # 1. read characters for sell
    # 2. read bench
    # 3. create priority
    # 4. Buy characters
    # 5. account for going gold
    def buyCharacters(self):
        forSale = ComputerEyes.getSubshots()
        vb = VirtualBoard()
        onBench = vb.getBench()
        compControl = ComputerInput()
        sortedList = []
        lowestCharacterName = ""
        for x in onBench:
            if x != None:
                if x.level > 1 and x.name not in self.goldList:
                    self.priorityList[x.name] += 2
                elif x.level == 1 and x.name not in self.goldList:
                    self.priorityList[x.name] += 1

        sortedList = sorted(self.priorityList,
                            key=self.priorityList.__getitem__)

        for x in sortedList:
            if x.name in forSale and None in onBench:
                compControl.buyCharacter(forSale.indexof(x.name))
                vb.addToBench(Character(x.name, None, 1))
                self.characterCountList[x.name] += 1
                self.checkForGold(x.name)
            elif x.name in forSale:
                lowestPriority = 100
                lowestCharacterLocation = -1
                for y in onBench:
                    if(self.priorityList[y.name] < lowestPriority):
                        lowestPriority = self.priorityList[y.name]
                        lowestCharacterLocation = y
                        lowestCharacterName = y.name
                compControl.sellCharacterFrombench(lowestCharacterLocation)
                vb.removeFromBench(lowestCharacterLocation)
                self.characterCountList[lowestCharacterName]

                compControl.buyCharacter(forSale.indexof(x.name))
                vb.addToBench(Character(x.name, None, 1))
                self.characterCountList[x.name] += 1
                self.checkForGold(x.name)
    # Checks to see

    def checkForGold(self, name):
        if self.characterCountList[name] > 8:
            self.goldList.append(name)
