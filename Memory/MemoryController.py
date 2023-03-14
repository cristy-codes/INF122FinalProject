from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QLabel, QInputDialog

from BaseGame.GameController import GameController
from BaseGame.Tile import Tile
from BaseGame.Score import Score
from Memory.MemoryEndingMessage import MemoryEndingMessage
# from Memory.MemoryScore import MemoryScore
from BaseGame.SaveScore import SaveScore

class MemoryController(GameController):
    def __init__(self, turn):
        super().__init__(turn)
        self.first_tile = None
        self.second_tile = None

        self.total_buttons = 16
        self.clicked_buttons = []
        self.matched_buttons = []

        self.game_over = False
        self.currScore = 0

        # # Update the scoreboard display
        # self.board.scoreboard.load_scores()

    ### called when the tile is clicked; houses all clicked functionality
    # CORE CLICK FUNCTIONALITY, ALL THIS STUFF HAPPENS ONCE A TILE IS CLICKED
    def processPlayerMove(self, tile: Tile):
        self.processPlayerInput(tile)
        self.pointSystem()
        self.gameOverCondition()

    def processPlayerInput(self, tile: Tile):
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
                    
                    
                # if the 2 clicked tiles don't match, flip them back over after a second
                else:
                    QTimer.singleShot(1000, self.hide_clicked_buttons)
    
    def pointSystem(self):
        self.currScore = len(self.matched_buttons * 5)
        self.board.scoreLabel.setText(str(self.currScore))

    def gameOverCondition(self):
        ####### CHECK GAME OVER #######
        # if all tiles are matched, output a win and the player's score. 
        if len(self.matched_buttons) == self.total_buttons:
            if self.board.timer is not None and self.board.timer.isActive():
                time_remaining = self.board.maxTime
                self.board.timer.stop()
                self.currScore += time_remaining
                self.board.itemAt(1).widget().setText(str(self.currScore))
                MemoryEndingMessage("You won! Your score is: " + str(self.currScore))
                self.save_score(self.currScore)
        elif not self.board.timer.isActive():
            self.board.timer.stop()
            self.board.itemAt(1).widget().setText(str(self.currScore))
            MemoryEndingMessage("You ran out of time! Your score is: " + str(self.currScore))
            self.save_score(self.currScore)

    def save_score(self, score):
      dialog = SaveScore(score, "MT")
      dialog.exec_()

    # hide the clicked buttons and stop tracking them
    def hide_clicked_buttons(self):
        for button in self.clicked_buttons:
            button.flip()
            button.setEnabled(True)
        self.clicked_buttons = [] 

