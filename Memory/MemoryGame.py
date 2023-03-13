import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDialog

from Memory.MemoryBoard import MemoryBoard
from Memory.MemoryConditions import MemoryConditions
from Memory.MemoryController import MemoryController
from Memory.MemoryTurn import MemoryTurn


class MemoryGame(QDialog):
    def __init__(self):
        super().__init__()
        # initialize conditions for the game
        self.conditions = MemoryConditions(9999)
        # initialize a game turn
        self.turn = MemoryTurn()
        # initialize the game controller
        self.controller = MemoryController(self.conditions, self.turn)
        # initialize the size of the board
        self.board = MemoryBoard(4, 4, self.controller.processPlayerMove)
        # assign the board to the game controller
        self.controller.setBoard(self.board)

        # set up the board with tiles
        self.setLayout(self.board)
        # set up the game window
        self.setWindowTitle("Match Tiles Game")
        self.setGeometry(50, 50, 200, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MemoryGame()
    window.show()
    sys.exit(app.exec())
