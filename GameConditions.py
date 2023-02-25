from abc import ABC, abstractmethod

class GameConditions(ABC):
    def __init__(self, maxTime):
        self.maxGameTime = maxTime
    
    def setMaxGameTime(self, maxTime:int):
        self.maxGameTime = maxTime

    def getMaxGameTime(self):
        return self.maxGameTime 

    @abstractmethod
    def determineGameOver(self):
        pass
