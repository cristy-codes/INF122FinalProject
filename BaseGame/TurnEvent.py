from abc import ABC, abstractmethod
from BaseGame import Board

class TurnEvent(ABC):
    def __init__(self):
        pass 

    # contains what happens during a turn within a game
    @abstractmethod
    def processTurn(self, board:Board):
        pass