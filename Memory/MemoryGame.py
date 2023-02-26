import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDialog

from Memory.MemoryBoard import MemoryBoard
from Memory.MemoryConditions import MemoryConditions
from Memory.MemoryController import MemoryController
from Memory.MemoryTurn import MemoryTurn


class MemoryGame(QDialog):
    def __init__(self):
        super().__init__()
        self.conditions = MemoryConditions(9999)
        self.turn = MemoryTurn()
        self.controller = MemoryController(self.conditions, self.turn)
        self.board = MemoryBoard(4, 4, self.controller.handler)
        self.controller.setBoard(self.board)
        # self.controller.start()

        self.setLayout(self.board)
        self.setWindowTitle("Match Tiles Game")
        self.setGeometry(50, 50, 200, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MemoryGame()
    window.show()
    sys.exit(app.exec())
