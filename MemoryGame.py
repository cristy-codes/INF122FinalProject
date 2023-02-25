import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from Board import Board

class MemoryGame(QDialog):
    def __init__(self):
        super().__init__()

        grid = Board()

        self.setLayout(grid)
        self.setWindowTitle("Match Tiles Game")
        self.setGeometry(50, 50, 200, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MemoryGame()
    window.show()
    sys.exit(app.exec())
