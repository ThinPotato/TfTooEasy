from character import Character
from computerInput import ComputerInput
import character
from computerEyes import ComputerEyes
from virtualBoard import VirtualBoard
from collections import defaultdict
from computerInput import ComputerInput
import sched
import time


class Build:

    def __init__(self):
        self.CE = ComputerEyes()

        # List of characters that are already at max level
        self.goldList = []

        # Characters nearly complete : priority + 2
        # native priority if is included : priority 1
        # priorityList only contains characters with at least 1 priority
        self.priorityList = defaultdict(int)
        self.characterCountList = defaultdict(int)

        # Priority board contains the reference for where characters should be placed
        self.priorityBoard = VirtualBoard()
        # Current board contains the live reading of what is on the board
        self.currentBoard = VirtualBoard()
        # Creates a Scheduler to check for a round start
        self.s = sched.scheduler(time.time, time.sleep)
        self.s.enter(60, 1, self.planningCheck, (self.s,))
        self.s.run()

    # takes a screenshot every second and checks if the round started.
    # TODO: react to round starting by calling playTurn()
    def planningCheck(self, sc):
        self.CE.checkForRoundStart()
        self.s.enter(1, 1, self.planningCheck, (sc,))

    # Turn playbook:
    # 1. Buy characters
    # 2. Place characters
    # 3. Collect items
    # 4. Place items
    # 5. buy Exp (if on turn xth turn)
    def playTurn(self):
        self.buyCharacters()
        self.placeCharacters()

    # Places any matches from bench to map
    # TODO: account for better star ratings
    # TODO: account for if character is already on the space in the map
    def placeCharacters(self):
        onBench = self.currentBoard.getBench()
        compControl = ComputerInput()
        for x in self.priorityBoard:
            for z in x:
                if z is not None:
                    for y in onBench:
                        if y is not None and z.name == y.name:
                            compControl.benchToMap(y, x, z)

    # Buy Playbook:
    # 1. read characters for sell
    # 2. read bench
    # 3. create priority
    # 4. Buy characters
    # 5. account for going gold

    def buyCharacters(self):
        forSale = ComputerEyes.getSubshots()
        onBench = self.currentBoard.getBench()
        compControl = ComputerInput()
        sortedList = []
        lowestCharacterName = ""
        # 3
        for x in onBench:
            if x != None:
                if x.level > 1 and x.name not in self.goldList:
                    self.priorityList[x.name] += 2
                elif x.level == 1 and x.name not in self.goldList:
                    self.priorityList[x.name] += 1

        sortedList = sorted(self.priorityList,
                            key=self.priorityList.__getitem__)
        # 4, 5
        for x in sortedList:
            if x.name in forSale and None in onBench:
                compControl.buyCharacter(forSale.indexof(x.name))
                self.currentBoard.addToBench(Character(x.name, None, 1))
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
                self.currentBoard.removeFromBench(lowestCharacterLocation)
                self.characterCountList[lowestCharacterName]

                compControl.buyCharacter(forSale.indexof(x.name))
                self.currentBoard.addToBench(Character(x.name, None, 1))
                self.characterCountList[x.name] += 1
                self.checkForGold(x.name)

    def checkForGold(self, name):
        if self.characterCountList[name] > 8:
            self.goldList.append(name)
