from abc import ABC, abstractmethod

class GameConditions():
    def __init__(self, maxTime):
        self.maxGameTime = maxTime
    
    # setter for game time
    def setMaxGameTime(self, maxTime:int):
        self.maxGameTime = maxTime

    # getter for game time
    def getMaxGameTime(self):
        return self.maxGameTime 

    # function that determines whether or not the game is still active or over
    @abstractmethod
    def gameOverCondition(self):
        pass
    
    # establishes what happens when a tile is clicked
    @abstractmethod
    def clickEvent(self):
        pass
    
    # calculates points
    @abstractmethod
    def pointSystem(self):
        pass