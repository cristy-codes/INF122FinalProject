import math
import random
from abc import ABC

from Board import Board
from Memory.MemoryTile import MemoryTile


class MemoryBoard(Board):
    def __init__(self, rows, cols, handler=print):
        super().__init__(rows, cols)
        self.rows = rows
        self.cols = cols
        self.handler = handler
        self.board_colors = []
        self.hiddenTiles = len(self.get_colors()) * 2

        for color in self.get_colors():
            self.board_colors.append(color)
            self.board_colors.append(color)

        self.setBoard()

    def createTile(self, row, col, color="white"):
        back_color = random.choice(self.board_colors)
        self.board_colors.remove(back_color)
        return MemoryTile(color, back_color, row, col, self.handler)

    def setBoard(self):
        board_colors = []

        for color in self.get_colors():
            board_colors.append(color)
            board_colors.append(color)

        for i in range(self.get_rows()):
            for j in range(self.get_cols()):
                self.addWidget(self.createTile(i, j), i, j)

    def determineGameOver(self):
        pass

    def clickEvent(self):
        pass

    def pointSystem(self):
        pass
