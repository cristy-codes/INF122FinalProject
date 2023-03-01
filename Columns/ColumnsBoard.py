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
    return ColumnsTile(self.getDefaultColor(), row, col, self.handler)

  def setStatusBar(self):
    self.statusLabel = QLabel("Score:")
    self.scoreLabel = QLabel("0")
    self.column = [ColumnsTile("white", 0, 0),
                   ColumnsTile("white", 0, 0),
                   ColumnsTile("white", 0, 0)]
    
    self.addWidget(self.statusLabel, 0, self.cols, 2, 4, Qt.Alignment())
    self.addWidget(self.scoreLabel, 2, self.cols, 2, 4, Qt.Alignment())
    self.addWidget(self.column[0], 4, self.cols+2)
    self.addWidget(self.column[1], 5, self.cols+2)
    self.addWidget(self.column[2], 6, self.cols+2)

  def getDefaultColor(self):
    return "white"
