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
        self.game_over = False
        self.board_colors = []
        self.hiddenTiles = len(self.get_colors()) * 2
        self.buttons = []

        for color in self.get_colors():
            self.board_colors.append(color)
            self.board_colors.append(color)
        
        self.remaining_time = 45
        self.timer_label = QLabel(f"Time remaining: {self.remaining_time} seconds.", None)
        self.addWidget(self.timer_label, self.get_rows(), 0, 1, self.get_cols())
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerCountdown)
        self.timer.start(1000)

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
                new_tile = self.createTile(i, j)
                self.addWidget(new_tile, i, j)
                self.buttons.append(new_tile)

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
                
    def timerCountdown(self):
        self.remaining_time -= 1
        self.timer_label.setText(f"Time remaining: {self.remaining_time} seconds.")
        if self.hiddenTiles == 0:
            self.timer.stop()
            QMessageBox.information(None, "Congratulations!", "You won the game!")
            

        elif self.remaining_time == 0:
            self.timer.stop()
            QMessageBox.information(None, "Time's up!", "You ran out of time.")

 