import sys

from PyQt5.QtWidgets import QApplication, QDialog
from Columns.ColumnsBoard import ColumnsBoard
from Columns.ColumnsController import ColumnsController
from Columns.ColumnsConditions import ColumnsConditions
from Columns.ColumnsTurn import ColumnsTurn


class ColumnsGame(QDialog):
    def __init__(self, rows=24, cols=6, maxTime=100):
        super().__init__()
        self.conditions = ColumnsConditions(maxTime)
        self.columnsTurn = ColumnsTurn()
        self.controller = ColumnsController(self.conditions, self.columnsTurn)
        self.board = ColumnsBoard(rows, cols, self.controller.handler)
        self.controller.setBoard(self.board)
        self.controller.start()

        self.setLayout(self.board)
        self.setWindowTitle("Columns")
        self.setGeometry(50, 50, 200, 200)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColumnsGame()
    window.show()
    sys.exit(app.exec())
