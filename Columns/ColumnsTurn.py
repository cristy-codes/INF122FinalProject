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

            #### USE TO DEBUG 3 same color column drop bug
            #color = random.choice(board.get_colors()[1:3])

            # set ith column tile to color
            board.column[i].setColor(color)
