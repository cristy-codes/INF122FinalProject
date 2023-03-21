import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDialog

from BaseGame.Game import Game

from Memory.MemoryBoard import MemoryBoard
from Memory.MemoryController import MemoryController


class MemoryGame(Game):
    def __init__(self):
        super().__init__()

    def start(self):
        self.setLayout(self.board)
        self.setWindowTitle("Match Tiles Game")
        self.setGeometry(50, 50, 200, 200)

    def buildBoard(self):
        self.board = MemoryBoard(4, 4, self.controller.processPlayerMove)
        self.controller.setBoard(self.board)

    def buildController(self):
        self.controller = MemoryController()
