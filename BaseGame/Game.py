from abc import abstractmethod
from PyQt5.QtWidgets import QDialog


class Game(QDialog):
    def __init__(self):
        super().__init__()
        self.board = None
        self.controller = None

        self.buildController()
        self.buildBoard()
        self.start()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def buildBoard(self):
        pass

    @abstractmethod
    def buildController(self):
        pass
