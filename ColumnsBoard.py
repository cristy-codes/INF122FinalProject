from PyQt5.QtWidgets import QGridLayout
from ColumnsTile import ColumnsTile


"""
ColumnsBoard : inherits from QGridLayout

@variable rows:int - the rows for the board
@variable cols:int - the cols for the board

@variable table:ColumnsTile[][] - for storing the state of the board
"""
class ColumnsBoard(QGridLayout):
  def __init__(self, rows=24, cols=6, handler=print):
    super().__init__()
    self.rows = rows
    self.cols = cols
    self.handler = handler
    self.table = [[None for _ in range(cols)] for _ in range(rows)]

    # Create all Tile and assign to table
    for row in range(rows):
      for col in range(cols):
        self.table[row][col] = self.createTile(row, col)
        self.addWidget(self.table[row][col], row, col)

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
  