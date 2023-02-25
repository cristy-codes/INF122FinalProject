class Score():
    def __init__(self):
        self.score = 0
    
    def addPoints(self, points:int):
        self.score += points 
    
    def subtractPoints(self, points:int):
        self.score -= points

    def getCurrentPoints(self):
        return self.score