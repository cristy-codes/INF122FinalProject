from Columns.ColumnsBoard import ColumnsBoard
from Columns.ColumnsTile import ColumnsTile
from BaseGame.GameConditions import GameConditions
from BaseGame.Score import Score


class ColumnsConditions(GameConditions):
  def __init__(self, maxTime):
    super().__init__(maxTime)

  def determineGameOver(self, board:ColumnsBoard):
    ### check if there is a tile doesn't have default color in top row
    for tile in board.table[0]:
      if not (tile.hasDefaultColor()):
        return True

    return False

  def clickEvent(self, tile:ColumnsTile, board:ColumnsBoard):
    ### moves the tiles down
    stop = 3

    while True:
      if (stop == board.get_rows() or not
          board.getTile(stop, tile.col).hasDefaultColor()):
        break
      stop += 1

    # swap the three lowest uncolored tiles with the three queued tiles
    swapColor(board.getTile(stop-3, tile.col), board.column[0])
    swapColor(board.getTile(stop-2, tile.col), board.column[1])
    swapColor(board.getTile(stop-1, tile.col), board.column[2])

  # remove matching tiles and continue drop and get points
  def pointSystem(self, score:Score, board:ColumnsBoard):
    # get points
    points = matchingAlgo(board)
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

def matchingAlgo(board:ColumnsBoard) -> int:
  return 0