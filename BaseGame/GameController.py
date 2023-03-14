from BaseGame.Board import Board
from BaseGame.GameConditions import GameConditions
from BaseGame.Tile import Tile
from BaseGame.TurnEvent import TurnEvent
from BaseGame.Score import Score
from PyQt5.QtWidgets import QMessageBox
from BaseGame.SaveScore import SaveScore

class GameController:
    def __init__(self, conditions:GameConditions, turn:TurnEvent):
        self.board = None
        self.conditions = conditions
        self.gameTurn = turn
        self.score = Score() ## for tracking score

    # set board variable
    def setBoard(self, board:Board):
        self.board = board

    # ### called when the tile is clicked; houses all clicked functionality
    # def processPlayerMove(self, tile:Tile):
    #     # do something when the tile is clicked
    #     self.conditions.clickEvent(tile, self.board)
    #     # calculate and add score
    #     self.conditions.pointSystem(self.score, self.board)
    #     # determine to either start another turn or end the game
    #     self.checkGameOver()

    ### mechanism to determine whether to end game or proceed to next turn
    # def checkGameOver(self):
    #     ### stop game if the game is over
    #     if (self.gameOverCondition()):
    #         self.stop()
    #         self.save_score(self.score.getCurrentPoints())

    #     ### iterate through another turn
    #     else:
    #         self.gameTurn.processTurn(self.board)
    
    ### start the game
    # def start(self):
    #     # run the first turn
    #     self.gameTurn.processTurn(self.board)
    
    ### stop the game 
    # def stop(self):
    #     # disable all tiles on the board
    #     for tileList in self.board.table:
    #         for tile in tileList:
    #             tile.disable()

    def save_score(self, score):
        dialog = SaveScore(score, "COL")
        dialog.exec_()

    