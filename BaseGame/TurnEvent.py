from abc import ABC, abstractmethod 

class TurnEvent(ABC):
    def __init__(self):
        pass 

    @abstractmethod
    def processTurn(self):
        pass