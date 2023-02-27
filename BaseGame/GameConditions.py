from abc import ABC, abstractmethod

class GameConditions():
    def __init__(self, maxTime):
        self.maxGameTime = maxTime
    
    def setMaxGameTime(self, maxTime:int):
        self.maxGameTime = maxTime

    def getMaxGameTime(self):
        return self.maxGameTime 

    @abstractmethod
    def determineGameOver(self):
        pass

    @abstractmethod
    def clickEvent(self):
        pass

    @abstractmethod
    def pointSystem(self):
        pass