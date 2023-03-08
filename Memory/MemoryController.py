from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel

from BaseGame.GameController import GameController
from BaseGame.Tile import Tile
from Memory.MemoryEndingMessage import MemoryEndingMessage


class MemoryController(GameController):
    def __init__(self, conditions, turn):
        super().__init__(conditions, turn)
        self.first_tile = None
        self.second_tile = None

        self.total_buttons = 16
        self.clicked_buttons = []
        self.matched_buttons = []

        self.game_over = False

    def stop_timer(self):
        self.board.timer.stop()

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
                    # if all tiles are matched, output a win and the player's score.
                    if len(self.matched_buttons) == self.total_buttons:
                        if self.board.timer is not None and self.board.timer.isActive():
                            time_remaining = self.board.timer.remainingTime()
                            self.stop_timer()
                            MemoryEndingMessage("You won! Your score is: " + str(8 * time_remaining))
                            self.board.itemAt(1).widget().setText(str(8 * time_remaining))
                # if the 2 clicked tiles don't match, flip them back over after a second
                else:
                    QTimer.singleShot(1000, self.hide_clicked_buttons)

    # hide the clicked buttons and stop tracking them
    def hide_clicked_buttons(self):
        for button in self.clicked_buttons:
            button.flip()
            button.setEnabled(True)
        self.clicked_buttons = [] 




#