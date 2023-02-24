import sys

from PyQt5.QtWidgets import QApplication, QDialog
from ColumnsBoard import ColumnsBoard
from ColumnsController import ColumnsController


class ColumnsGame(QDialog):
    def __init__(self, rows=24, cols=6):
        super().__init__()
        self.controller = ColumnsController()
        self.board = ColumnsBoard(rows, cols, self.controller.handler)
        self.controller.setBoard(self.board)

        self.setLayout(self.board)
        self.setWindowTitle("Columns")
        self.setGeometry(50, 50, 200, 200)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColumnsGame()
    window.show()
    sys.exit(app.exec())
