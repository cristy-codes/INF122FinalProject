from BaseGame.TurnEvent import TurnEvent
from Columns.ColumnsBoard import ColumnsBoard
import random


class ColumnsTurn(TurnEvent):
    # def __init__(self):
    #     pass

    def processTurn(self, board: ColumnsBoard):
        ### create new column
        for i in range(3):
            color = random.choice(board.get_colors())
            board.column[i].setColor(color)
