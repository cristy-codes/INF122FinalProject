import random

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QMessageBox, QLabel
from BaseGame.Board import Board
from Memory.MemoryTile import MemoryTile


class MemoryBoard(Board):
    def __init__(self, rows, cols, handler=print):
        super().__init__(rows, cols)
        self.rows = rows
        self.cols = cols
        self.handler = handler
        self.board_colors = []
        self.buttons = []

        # double up the colors to enable matching
        for color in self.get_colors():
            self.board_colors.append(color)
            self.board_colors.append(color)

        self.maxTime = 2

        # set the board
        self.setBoard()
        # create the timer object
        self.createTimer(self.maxTime, self.timerCountdown)
        # reveal the tiles
        self.reveal()

    # show all tiles for a second
    def reveal(self):
        for button in self.buttons:
            button.flip()
        QTimer.singleShot(1000, self.hide_tiles)

    # hide all tiles
    def hide_tiles(self):
        for button in self.buttons:
            button.flip()

    ######################################    
    # create an individual tile
    def createTile(self, row, col, color="white"):
        back_color = random.choice(self.board_colors)
        self.board_colors.remove(back_color)
        return MemoryTile(color, back_color, row, col, self.handler)

    ######################################
    # set the playable area
    def setBoard(self):
        board_colors = []
        for color in self.get_colors():
            board_colors.append(color)
            board_colors.append(color)

        for i in range(self.get_rows()):
            for j in range(self.get_cols()):
                # new_tile = self.createTile(i, j)
                # self.table[i][j] = new_tile
                self.table[i][j] = self.createTile(i, j)
                self.addWidget(self.table[i][j], i, j)
                self.buttons.append(self.table[i][j])

    # Function that is called every second (that the timer counts down)
    # def timerCountdown(self):
    #     # sets the label to remaining time left, subtracts time
    #     self.decrementTime()
    #     # if there is no more time remaining, declare a
    #     # game loss.
    #     if self.maxTime == 0:
    #         self.timer.stop()
    #         QMessageBox.information(None, "Time's up!", "You ran out of time.")






 