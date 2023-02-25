import random
from ColumnsBoard import ColumnsBoard
from ColumnsTile import ColumnsTile

"""
ColumnsConditions sets the conditions for the game

@method winCondition - the condition to check if the game is won
@method loseCondition - the condition to check if the game is lost
@method turnCondition - the condition to run for each turn
"""
class ColumnsConditions():
  def __init__(self):
    self.time = 100_000
    self.colors = ["black", "cyan", "green", "red", "yellow", "magenta", "blue", "gray"]

  """
  Color to set all tiles initially
  """
  def defaultColor(self):
    return "white"

  """
  Maximum allowed time to run game
  """
  def maxTime(self):
    return self.time

  """
  Condition to meet if a win
  """
  def winCondition(self, board:ColumnsBoard):
    return False

  """
  Condition to meet if a lose
  """
  def loseCondition(self, board:ColumnsBoard):
    result = False

    ### check if there is a tile doesn't have default color in fourth row
    for tile in board.table[3]:
      if (tile.getColor() != self.defaultColor()):
        result = True

    return result

  """
  Event at the beggining of every turn
  """
  def turnEvent(self, board:ColumnsBoard):
    ### create new column
    for i in range(3):
      color = random.choice(self.colors)
      board.getTile(i, board.getCols()//2).setColor(color)
      board.column[i].setColor(color)

  """
  Event to execute after click on tile
  """
  def clickEvent(self, tile:ColumnsTile, board:ColumnsBoard):
    ### moves the tiles down
    stop = 3

    while True:
      if (stop == board.getRows() or
          board.getTile(stop, tile.col).getColor() != self.defaultColor()): # there's a colored block or is last row
        break
      stop += 1

    self.swapColor(board.getTile(stop-3, tile.col), board.getTile(0, board.getCols()//2))
    self.swapColor(board.getTile(stop-2, tile.col), board.getTile(1, board.getCols()//2))
    self.swapColor(board.getTile(stop-1, tile.col), board.getTile(2, board.getCols()//2))

  """
  System for points and game logic, such as erasing each match and adding score.
  """
  def pointSystem(self, board:ColumnsBoard):
    pass

  ### HELPER functions
  def swapColor(self, tileFrom:ColumnsTile, tileTo:ColumnsTile):
    temp = tileFrom.getColor()
    tileFrom.setColor(tileTo.getColor())
    tileTo.setColor(temp)
