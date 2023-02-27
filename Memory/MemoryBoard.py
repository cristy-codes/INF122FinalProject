import random

from PyQt5.QtCore import QTimer

from BaseGame.Board import Board
from Memory.MemoryTile import MemoryTile


class MemoryBoard(Board):
    def __init__(self, rows, cols, handler=print):
        super().__init__(rows, cols)
        self.rows = rows
        self.cols = cols
        self.handler = handler
        self.board_colors = []
        self.hiddenTiles = len(self.get_colors()) * 2
        self.buttons = []

        for color in self.get_colors():
            self.board_colors.append(color)
            self.board_colors.append(color)

        self.setBoard()
        self.reveal()

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
                tile = self.createTile(i, j)
                self.addWidget(tile, i, j)
                self.buttons.append(tile)

    def determineGameOver(self):
        pass

    def clickEvent(self):
        pass

    def pointSystem(self):
        pass

    def reveal(self):
        for button in self.buttons:
            button.flip()
        QTimer.singleShot(1000, self.hide_tiles)

    def hide_tiles(self):
        for button in self.buttons:
            button.flip()
