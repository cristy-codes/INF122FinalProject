from abc import ABC, abstractmethod 

class TurnEvent(ABC):
    def __init__(self):
        pass 

    # contains what happens during a turn within a game
    @abstractmethod
    def processTurn(self):
        pass