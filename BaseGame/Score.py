class Score():
    def __init__(self):
        self.score = 0
    
    # add points
    def addPoints(self, points:int):
        self.score += points 
    
    # subtract points
    def subtractPoints(self, points:int):
        self.score -= points

    # getter for current points
    def getCurrentPoints(self):
        return self.score
    
    