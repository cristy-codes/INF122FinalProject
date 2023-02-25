from ColumnsBoard import ColumnsBoard
from ColumnsTile import ColumnsTile
from ColumnsConditions import ColumnsConditions

"""
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
    self.conditions.pointSystem(self.board)
    self.gameLoop()

  def gameLoop(self):
    # Game is Lost
    if (self.conditions.winCondition(self.board)):
      print("WON")
      self.stop()
    elif (self.conditions.loseCondition(self.board)):
      print("LOST")
      self.stop()
    else:
      self.conditions.turnEvent(self.board)

  def start(self):
    self.conditions.turnEvent(self.board)

  def stop(self):
    for tileList in self.board.table:
      for tile in tileList:
        tile.disable()

  