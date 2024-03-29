from PyQt5.QtCore import QTimer

from BaseGame.GameController import GameController
from BaseGame.Tile import Tile
from BaseGame.Score import Score
from BaseGame.GameEndingMessage import GameEndingMessage
from Memory.MemoryBoard import MemoryBoard


class MemoryController(GameController):
    def __init__(self):
        super().__init__()
        self.first_tile = None
        self.second_tile = None

        self.total_buttons = 16
        self.clicked_buttons = []
        self.matched_buttons = []

    def processPlayerClick(self, tile: Tile, board: MemoryBoard):
        # if the tile is facedown, flip it and track which tile is clicked
        if tile.face_down:
            tile.flip()
            tile.setEnabled(False)
            self.clicked_buttons.append(tile)

            if len(self.clicked_buttons) == 2:
                # if the 2 clicked tiles match then track and clear them
                if self.clicked_buttons[0].color == self.clicked_buttons[1].color:
                    self.clicked_buttons[0].clearTile()
                    self.clicked_buttons[1].clearTile()

                    self.clicked_buttons[0].disable()
                    self.clicked_buttons[1].disable()

                    self.matched_buttons.append(self.clicked_buttons[0])
                    self.matched_buttons.append(self.clicked_buttons[1])

                    self.clicked_buttons = []

                # if the 2 clicked tiles don't match, flip them back over after a second
                else:
                    QTimer.singleShot(500, self.hide_clicked_buttons)

    def pointSystem(self, score: Score, board: MemoryBoard):
        # calculates the current score based on number of matched tiles
        score.setCurrentPoints(len(self.matched_buttons * 5))
        board.scoreLabel.setText(str(score.getCurrentPoints()))

    def gameOverCondition(self):
        ####### CHECK GAME OVER #######
        # if all tiles are matched, output a win and the player's score. 
        if len(self.matched_buttons) == self.total_buttons:
            if self.board.timer is not None and self.board.timer.isActive():
                time_remaining = self.board.maxTime
                self.board.timer.stop()
                self.score.addPoints(time_remaining)
                self.board.itemAt(1).widget().setText(str(self.score.getCurrentPoints()))
                GameEndingMessage("You won! Your score is: " + str(self.score.getCurrentPoints()))
                self.save_score(self.score.getCurrentPoints(), "MT")
        # if there is no more time left, output a "loss" and the player's score
        elif not self.board.timer.isActive():
            self.board.timer.stop()
            self.board.itemAt(1).widget().setText(str(self.score.getCurrentPoints()))
            GameEndingMessage("You ran out of time! Your score is: " + str(self.score.getCurrentPoints()))
            self.save_score(self.score.getCurrentPoints(), "MT")

    # hide the clicked buttons and stop tracking them
    def hide_clicked_buttons(self):
        for button in self.clicked_buttons:
            button.flip()
            button.setEnabled(True)
        self.clicked_buttons = []
