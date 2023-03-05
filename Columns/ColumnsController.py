from Columns.ColumnsConditions import ColumnsConditions
from Columns.ColumnsTurn import ColumnsTurn
from BaseGame.GameController import GameController
from PyQt5.QtCore import QTimer, QDateTime


class ColumnsController(GameController):
    def __init__(self, conditions: ColumnsConditions, columnsTurn: ColumnsTurn):
        super().__init__(conditions, columnsTurn)

    # starts GameController and timer
    def start(self):
        super().start()
        self.board.timerStart()

    # stops GameController and timer
    def stop(self):
        super().stop()
        self.board.timerStop()
