from ColumnsBoard import ColumnsBoard
from ColumnsTile import ColumnsTile
from ColumnsConditions import ColumnsConditions
from ColumnsTurn import ColumnsTurn
from GameController import GameController

"""
ColumnsController class
"""
class ColumnsController(GameController):
  def __init__(self, conditions:ColumnsConditions, columnsTurn:ColumnsTurn):
    # self.columnsTurn = ColumnsTurn()  # im not too sure about this, it kinda seems like a copout to use ColumnsTurn like this
    super().__init__(conditions, columnsTurn)
    # self.board = None
    # self.conditions = conditions
    # self.columnsTurn = ColumnsTurn() # im not too sure about this, it kinda seems like a copout to use ColumnsTurn like this

  # def setBoard(self, board:ColumnsBoard):
  #   self.board = board

  # def handler(self, tile:ColumnsTile):
  #   self.conditions.clickEvent(tile, self.board)
  #   self.conditions.pointSystem(self.board)
  #   self.gameLoop()

  # def gameLoop(self):
  #   ### stop game if the game is over
  #   if (self.conditions.determineGameOver(self.board)):
  #     print("GAME OVER")
  #     self.stop()
  #   ### iterate through another turn
  #   else:
  #     self.columnsTurn.processTurn(self.board)

  # def start(self):
  #   self.columnsTurn.processTurn(self.board)

  # def stop(self):
  #   for tileList in self.board.table:
  #     for tile in tileList:
  #       tile.disable()

  