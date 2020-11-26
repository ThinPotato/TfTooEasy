from array import *
import character


class VirtualBoard:

    def __init__(self):
        # 4x7 2d array containing characters or null
        self.board = [
            [None] * 7,
            [None] * 7,
            [None] * 7,
            [None] * 7]
        # 1*9 array containing characters or null
        self.bench = [None] * 9

    def addToBoard(self, char, x, y):
        if self.board[x][y] is None:
            self.board[x][y] = char
        else:
            temp = self.board[x][y]
            self.board[x][y] = char
            self.addtoBench(temp)

    def removeFromBoard(self, x, y):
        temp = self.board[x][y]
        self.board[x][y] = None
        return temp

    def addToBench(self, char):
        for space in self.bench:
            if self.bench[space] is None:
                self.benh[space] = char
                break

    def removeFromBench(self, space):
        temp = self.bench[space]
        self.bench[space] = None
        return temp

    def getBench(self):
        return self.bench
