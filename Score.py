class Score():
    def __init__(self):
        self.currentScore = 0
    
    def addPoints(self, points:int):
        self.currentScore += points 
    
    def subtractPoints(self, points:int):
        self.currentScore -= points

    def getCurrentPoints(self):
        return self.currentScore