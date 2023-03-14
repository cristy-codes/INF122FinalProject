from BaseGame.Board import Board
from BaseGame.GameConditions import GameConditions
from BaseGame.Tile import Tile
from BaseGame.TurnEvent import TurnEvent
from BaseGame.Score import Score
from PyQt5.QtWidgets import QMessageBox
from BaseGame.SaveScore import SaveScore

class GameController:
    def __init__(self, turn:TurnEvent):
        self.board = None
        # self.conditions = conditions
        self.gameTurn = turn
        self.score = Score() ## for tracking score

    # set board variable
    def setBoard(self, board:Board):
        self.board = board
    