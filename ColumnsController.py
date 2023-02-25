from ColumnsBoard import ColumnsBoard
from ColumnsTile import ColumnsTile
from ColumnsConditions import ColumnsConditions
from ColumnsTurn import ColumnsTurn

"""
ColumnsController class
"""
class ColumnsController:
  def __init__(self, conditions:ColumnsConditions):
    self.board = None
    self.conditions = conditions
    self.columnsTurn = ColumnsTurn()

  def setBoard(self, board:ColumnsBoard):
    self.board = board

  def handler(self, tile:ColumnsTile):
    self.conditions.clickEvent(tile, self.board)
    self.conditions.pointSystem(self.board)
    self.gameLoop()

  def gameLoop(self):
    ### stop game if the game is over
    if (self.conditions.determineGameOver(self.board)):
      print("GAME OVER")
      self.stop()
    ### iterate through another turn
    else:
      self.conditions.turnEvent(self.board)
      # self.columnsTurn.processTurn(self.board)

  def start(self):
    self.conditions.turnEvent(self.board)
    # self.columnsTurn.processTurn(self.board)

  def stop(self):
    for tileList in self.board.table:
      for tile in tileList:
        tile.disable()

  