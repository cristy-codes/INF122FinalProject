from TurnEvent import TurnEvent 
from ColumnsBoard import ColumnsBoard
import random

class ColumnsTurn(TurnEvent):
    def __init__(self):
        pass 

    def processTurn(self, board:ColumnsBoard):
        ### create new column
        for i in range(3):
            color = random.choice(self.colors)
            board.column[i].setColor(color)