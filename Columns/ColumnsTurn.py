from BaseGame.TurnEvent import TurnEvent
from Columns.ColumnsBoard import ColumnsBoard
import random


class ColumnsTurn(TurnEvent):
    # action performed during a turn
    def processTurn(self, board: ColumnsBoard):
        # create new column of three
        for i in range(3):
            # get a random color out of six colors
            color = random.choice(board.get_colors()[1:7])
            # set ith column tile to color
            board.column[i].setColor(color)
