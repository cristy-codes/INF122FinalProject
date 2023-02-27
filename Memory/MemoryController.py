from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

from BaseGame.GameController import GameController
from BaseGame.Tile import Tile

import time


class MemoryController(GameController):
    def __init__(self, conditions, turn):
        super().__init__(conditions, turn)
        self.first_tile = None
        self.second_tile = None

        self.total_buttons = 16
        self.clicked_buttons = []
        self.matched_buttons = []

    def handler(self, tile: Tile):
        if tile.face_down:
            tile.flip()
            tile.setEnabled(False)
            self.clicked_buttons.append(tile)

            if len(self.clicked_buttons) == 2:
                if self.clicked_buttons[0].color == self.clicked_buttons[1].color:
                    self.matched_buttons.extend(self.clicked_buttons)
                    self.clicked_buttons = []
                    if len(self.matched_buttons) == self.total_buttons:
                        print("You win!")
                else:
                    QTimer.singleShot(1000, self.hide_clicked_buttons)

    def hide_clicked_buttons(self):
        for button in self.clicked_buttons:
            button.flip()
            button.setEnabled(True)
        self.clicked_buttons = []
