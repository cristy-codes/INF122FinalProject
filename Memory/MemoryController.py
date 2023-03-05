from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

from BaseGame.GameController import GameController
from BaseGame.Tile import Tile

from Memory.MemoryVictory import MemoryVictory

import time


class MemoryController(GameController):
    def __init__(self, conditions, turn):
        super().__init__(conditions, turn)
        self.first_tile = None
        self.second_tile = None

        self.total_buttons = 16
        self.clicked_buttons = []
        self.matched_buttons = []

        self.game_over = False  
    
    ### called when the tile is clicked; houses all clicked functionality
    def handler(self, tile: Tile):
        '''
        STRUCTURE FROM GAMECONTROLLER

        # do something when the tile is clicked
        self.conditions.clickEvent(tile, self.board)
        # calculate and add score
        self.conditions.pointSystem(self.score, self.board)
        # determine to either start another turn or end the game
        self.gameLoop()

        '''
        if tile.face_down:
            # if the tile is facedown, flip it and track which tile is clicked
            tile.flip()
            tile.setEnabled(False)
            self.clicked_buttons.append(tile)

            if len(self.clicked_buttons) == 2:
                # if the 2 clicked tiles match then track them
                if self.clicked_buttons[0].color == self.clicked_buttons[1].color:
                    self.matched_buttons.extend(self.clicked_buttons)
                    self.clicked_buttons = []
                    # if all tiles are matched, output a win
                    if len(self.matched_buttons) == self.total_buttons:
                        MemoryVictory("You won!")
                # if the 2 clicked tiles don't match, flip them back over after a second
                else:
                    QTimer.singleShot(1000, self.hide_clicked_buttons)

    # hide the clicked buttons and stop tracking them
    def hide_clicked_buttons(self):
        for button in self.clicked_buttons:
            button.flip()
            button.setEnabled(True)
        self.clicked_buttons = [] 
