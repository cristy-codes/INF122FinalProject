
from BaseGame.Game import Game

from Columns.ColumnsBoard import ColumnsBoard
from Columns.ColumnsController import ColumnsController


class ColumnsGame(Game):
    def __init__(self, rows=24, cols=6, maxTime=100):
        self.rows = 24
        self.cols = 6
        super().__init__()

    def start(self):
        self.controller.start()
        self.setLayout(self.board)
        self.setWindowTitle("Columns")
        self.setGeometry(50, 50, 200, 200)

    def buildBoard(self):
        # Create a Board with the specified dimensions
        self.board = ColumnsBoard(self.rows, self.cols, self.controller.processPlayerMove)
        self.controller.setBoard(self.board)

    def buildController(self):
        self.controller = ColumnsController()
