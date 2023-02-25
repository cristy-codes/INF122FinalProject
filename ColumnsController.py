from ColumnsConditions import ColumnsConditions
from ColumnsBoard import ColumnsBoard
from ColumnsTile import ColumnsTile

"""
callable class

ColumnsController class


"""
class ColumnsController:
  def __init__(self, conditions:ColumnsConditions):
    self.board = None
    self.conditions = conditions

  def setBoard(self, board:ColumnsBoard):
    self.board = board

  def handler(self, tile:ColumnsTile):
    self.conditions.clickEvent(tile, self.board)
    self.gameLoop()

  def moveDown(self, row:int, col:int):
    pass

  def changeColor(self, tile:ColumnsTile, color):
    tile.setColor(color)

  def start(self):
    self.conditions.turnEvent(self.board)

  def gameLoop(self):
    self.conditions.turnEvent(self.board)
    # Game is Lost
    if (self.conditions.winCondition(self.board)):
      print("WON")

    if (self.conditions.loseCondition(self.board)):
      print("LOST")
