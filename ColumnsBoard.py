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
  def __init__(self, rows, cols, handler=print):
    super().__init__()
    self.rows = rows
    self.cols = cols
    self.handler = handler
    self.table = [[None for _ in range(cols)] for _ in range(rows)]
    self.setBoard()
    self.setStatus()

  # Create all Tile and assign to table
  def setBoard(self):
    for row in range(self.rows):
      for col in range(self.cols):
        self.table[row][col] = self.createTile(row, col)
        self.addWidget(self.table[row][col], row, col)


  def setStatus(self):
    self.scoreLabel = QLabel("Temp Score")
    self.column = [ColumnsTile("white", 0, 0),
                   ColumnsTile("white", 0, 0),
                   ColumnsTile("white", 0, 0)]
    
    self.addWidget(self.scoreLabel, 0, self.cols, 2, 4, Qt.Alignment())
    self.addWidget(self.column[0], 2, self.cols+2)
    self.addWidget(self.column[1], 3, self.cols+2)
    self.addWidget(self.column[2], 4, self.cols+2)


  def getRows(self):
    return self.rows

  def getCols(self):
    return self.cols

  def getTile(self, row:int, col:int) -> ColumnsTile:
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

  def createTile(self, row, col, color="white"):
    return ColumnsTile(color, row, col, self.handler)
