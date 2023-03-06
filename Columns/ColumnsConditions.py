from Columns.ColumnsBoard import ColumnsBoard
from Columns.ColumnsTile import ColumnsTile
from BaseGame.GameConditions import GameConditions
from BaseGame.Score import Score


class ColumnsConditions(GameConditions):
  def __init__(self, maxTime):
    super().__init__(maxTime)

  # check if there is a tile doesn't have default color in top row
  def determineGameOver(self, board:ColumnsBoard):
    for tile in board.table[0]:
      if not (tile.hasDefaultColor()):
        return True
    return False

  # drop the three queued tiles on the tile's column
  def clickEvent(self, tile:ColumnsTile, board:ColumnsBoard):
    # set tiles from queue to the top three rows in the tile's column
    swapColor(board.getTile(0, tile.col), board.column[0])
    swapColor(board.getTile(1, tile.col), board.column[1])
    swapColor(board.getTile(2, tile.col), board.column[2])
    # gravity fall column, to drop tiles to bottom
    fallColumn(board, tile.col)

  # remove matching tiles and continue drop and get points
  def pointSystem(self, score:Score, board:ColumnsBoard):
    # get points
    points = matchingAlgorithm(board)
    # set points
    score.addPoints(self.pointFactor(points))
    # display points
    board.scoreLabel.setText(str(score.getCurrentPoints())) # set new score

  # each block is 50 points, times factor if more than 3
  def pointFactor(self, score:int) -> int:
    PPB = 50
    return round((1.05**score) * score*PPB) if (score>3) else (score*PPB)

### HELPER functions ###

def swapColor(tileFrom:ColumnsTile, tileTo:ColumnsTile):
  temp = tileFrom.getColor()
  tileFrom.setColor(tileTo.getColor())
  tileTo.setColor(temp)

def matchingAlgorithm(board:ColumnsBoard) -> int:
  # for row in range(board.get_rows()):
  #   for col in range(board.get_cols()):
  return 0 

# Drop all tiles to bottom for one column (like gravity), 
# starts from bottom (row ##), moves to top (row 0).
# Based on a sliding window algorithm, find tile that is default color (start) and tile 
# that is non-default color (stop), swap them and continue search from start
def fallColumn(board:ColumnsBoard, col:int):
  start = board.get_rows()-1 # get bottom row
  stop = start
  # until stop is out-of-bounds, meaning that there is no more colored tiles that should be dropped
  while not stop < 0:
    # if start is not a default color tile, move both up 
    if not board.getTile(start, col).hasDefaultColor():
      start -= 1 # move up
      stop -= 1 # move up
    # if stop is a default color tile, move stop up
    elif board.getTile(stop, col).hasDefaultColor():
      stop -= 1 # move up
    # both, start is a non-default color and stop is a non-default color
    else:
      swapColor(board.getTile(start, col), board.getTile(stop, col)) # swap colors
      stop = start # reset stop, to continue drops from start
