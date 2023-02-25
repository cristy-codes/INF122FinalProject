from PyQt5.QtWidgets import QGridLayout, QLabel
from ColumnsTile import ColumnsTile
from PyQt5.QtCore import Qt


"""
ColumnsBoard : inherits from QGridLayout

@variable rows:int - the rows for the board
@variable cols:int - the cols for the board

@variable table:ColumnsTile[][] - for storing the state of the board
"""
class ColumnsBoard(QGridLayout):
  def __init__(self, rows=24, cols=8, handler=print):
    super().__init__()
    self.rows = rows
    self.cols = cols
    self.handler = handler
    self.table = [[None for _ in range(cols)] for _ in range(rows)]
    scoreLabel = QLabel("Temp Score")

    # Create all Tile and assign to table
    for row in range(rows):
      for col in range(cols - 2):
        self.table[row][col] = self.createTile(row, col)
        self.addWidget(self.table[row][col], row, col)

    # self.addWidget(self.createTile(0, 6), 0, 6)

    self.addWidget(scoreLabel, 0, 6, 1, 2, Qt.Alignment())
    self.addWidget(self.createTile(1, 7), 1, 7)
    self.addWidget(self.createTile(2, 7), 2, 7)
    self.addWidget(self.createTile(3, 7), 3, 7)


  def getRows(self):
    return self.rows

  def getCols(self):
    return self.cols

  def getTile(self, row:int, col:int) -> ColumnsTile | None:
    return self.table[row][col]
  
  def addTile(self, row:int, col:int):
    if ((0 <= row) and (row < self.rows) and 
        (0 <= col) and (col < self.cols) and 
        (self.table[row][col] == None)):
      self.table[row][col] = self.createTile(row, col)
      self.addWidget(self.table[row][col], row, col)

  def removeTile(self, row:int, col:int):
    if ((0 <= row) and (row < self.rows) and 
        (0 <= col) and (col < self.cols) and 
        (self.table[row][col] != None)):
      self.removeWidget(self.table[row][col])
      self.table[row][col] = None

  def createTile(self, row, col):
    return ColumnsTile("white", row, col, self.handler)
