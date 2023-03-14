from abc import ABC, abstractmethod

from BaseGame import Board
from BaseGame import Score
from BaseGame import Tile


class GameConditions():
    def __init__(self, maxTime):
        self.maxGameTime = maxTime

    # setter for game time
    # def setMaxGameTime(self, maxTime: int):
    #     self.maxGameTime = maxTime

    # # getter for game time
    # def getMaxGameTime(self):
    #     return self.maxGameTime

    # # establishes what happens when a tile is clicked
    # @abstractmethod
    # def clickEvent(self, tile: Tile, board: Board):
    #     pass

    # # calculates points
    # @abstractmethod
    # def pointSystem(self, score: Score, board: Board):
    #     pass
    
    # # function that determines whether or not the game is still active or over
    # @abstractmethod
    # def gameOverCondition(self, board: Board):
    #     pass