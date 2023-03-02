from PyQt5.QtWidgets import QLabel
from Columns.ColumnsTile import ColumnsTile
from PyQt5.QtCore import Qt
from BaseGame.Board import Board


class ColumnsBoard(Board):
  def __init__(self, rows, cols, handler=print):
    super().__init__(rows, cols)
    self.handler = handler
    self.setBoard()
    self.setStatusBar()

  def setBoard(self):
    for row in range(self.rows):
      for col in range(self.cols):
        self.table[row][col] = self.createTile(row, col)
        self.addWidget(self.table[row][col], row, col)

  def createTile(self, row, col):
    return ColumnsTile(row, col, None, self.handler)

  def setStatusBar(self):
    self.statusLabel = QLabel("Score:")
    self.scoreLabel = QLabel("0")
    self.column = [ColumnsTile("white", 0, 0),
                   ColumnsTile("white", 0, 0),
                   ColumnsTile("white", 0, 0)]
    
    self.addWidget(self.statusLabel, 0, self.cols, 2, 1, Qt.Alignment())
    self.addWidget(self.scoreLabel, 0, self.cols+2, 2, 1, Qt.Alignment())
    self.addWidget(self.column[0], 3, self.cols+2)
    self.addWidget(self.column[1], 4, self.cols+2)
    self.addWidget(self.column[2], 5, self.cols+2)
