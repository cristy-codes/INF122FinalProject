from ColumnsBoard import ColumnsBoard
from ColumnsTile import ColumnsTile

"""
callable class

ColumnsController class


"""
class ColumnsController:
  def __init__(self):
    self.board = None

  def setBoard(self, board:ColumnsBoard):
    self.board = board

  def handler(self, tile:ColumnsTile):
    print(tile.row, tile.col, self)
    self.changeColor(tile, "black")

  def moveDown(self, row:int, col:int):
    pass

  def changeColor(self, tile:ColumnsTile, color):
    tile.setColor(color)

