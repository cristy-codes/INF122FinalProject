from BaseGame.Board import Board
from BaseGame.GameConditions import GameConditions
from BaseGame.Tile import Tile
from BaseGame.TurnEvent import TurnEvent
from BaseGame.Score import Score
from PyQt5.QtWidgets import QMessageBox

class GameController:
    def __init__(self, conditions:GameConditions, turn:TurnEvent):
        self.board = None
        self.conditions = conditions
        self.gameTurn = turn
        self.score = Score() ## for tracking score

    # set board variable
    def setBoard(self, board:Board):
        self.board = board

    ### called when the tile is clicked; houses all clicked functionality
    def handler(self, tile:Tile):
        # do something when the tile is clicked
        self.conditions.clickEvent(tile, self.board)
        # calculate and add score
        self.conditions.pointSystem(self.score, self.board)
        # determine to either start another turn or end the game
        self.gameLoop()

    ### mechanism to determine whether to end game or proceed to next turn
    def gameLoop(self):
        ### stop game if the game is over
        if (self.conditions.determineGameOver(self.board)):
            QMessageBox.information(None, "GAME OVER!", "You ran out of space!")
            self.stop()
        ### iterate through another turn
        else:
            self.gameTurn.processTurn(self.board)
    
    ### start the game
    def start(self):
        # run the first turn
        self.gameTurn.processTurn(self.board)
    
    ### stop the game 
    def stop(self):
        # disable all tiles on the board
        for tileList in self.board.table:
            for tile in tileList:
                tile.disable()