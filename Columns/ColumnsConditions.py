from Columns.ColumnsBoard import ColumnsBoard
from Columns.ColumnsTile import ColumnsTile
from BaseGame.GameConditions import GameConditions
from BaseGame.Score import Score


class ColumnsConditions(GameConditions):
  def __init__(self, maxTime):
    super().__init__(maxTime)

  def determineGameOver(self, board:ColumnsBoard):
    result = False

    ### check for timer value here
    self.getMaxGameTime()

    ### check if there is a tile doesn't have default color in top row
    for tile in board.table[0]:
      if not (tile.hasDefaultColor()):
        result = True

    return result

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
    points = scoreAlgorithm(board, board.get_rows()-1)
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

# when called, start row from highest number, meaning it goes bottom-up
def scoreAlgorithm(board:ColumnsBoard, row:int) -> int:
  if (row < 0): # no more rows
    return 0
  for i in range(board.get_cols()):
    # match check for non-default-color tiles
    if not board.getTile(row, i).hasDefaultColor():
      color = board.getTile(row, i).getColor()
      for rowT in range (-1, 1): # -1 and 0, bottom-up no need to re-look down
        for colT in range (-1, 2): # -1 to 1
          depth = continueSearch(board, color, row, i, rowT, colT)
          if (depth > 2): # 3 or more continous matches
            # remove tiles
            removeMatches(board, color, row, i, rowT, colT)
            # return score as depth and recursion
            return depth + scoreAlgorithm(board, row)

  return scoreAlgorithm(board, row-1) # move to next row

# Get depth of search one way
def continueSearch(board:ColumnsBoard, color:str, row:int, col:int, rowT:int, colT:int):
  newRow = row+rowT
  newCol = col+colT
  if ((rowT != 0 or colT != 0) and # to prevent self search infinity
      newRow >= 0 and newRow < board.get_rows() and  # to prevent out-of-row 
      newCol >= 0 and newCol < board.get_cols() and  # to prevent out-of-col 
      board.getTile(newRow, newCol).getColor() == color): # if matches
    return 1 + continueSearch(board, color, newRow, newCol, rowT, colT)
  return 1

# Recursive path remove
def removeMatches(board:ColumnsBoard, color:str, row:int, col:int, rowT:int, colT:int):
  newRow = row+rowT
  newCol = col+colT
  if (newRow >= 0 and newRow < board.get_rows() and  # to prevent out-of-row 
      newCol >= 0 and newCol < board.get_cols() and  # to prevent out-of-col 
      board.getTile(newRow, newCol).getColor() == color): # if matches
    removeMatches(board, color, newRow, newCol, rowT, colT)
  board.getTile(row, col).setDefaultColor() # set row and col to default
  fallRow(board, row, col)

# get row and col and starts falling tiles
def fallRow(board:ColumnsBoard, row:int, col:int):
  start = row
  while True:
    if (start == 0 or
        board.getTile(start, col).hasDefaultColor()):
      break
    start -= 1
  stop = start
  while True:
    if (stop == 0 or not
        board.getTile(stop, col).hasDefaultColor()):
      break
    stop -= 1
  while (stop >= 0 and not board.getTile(stop, col).hasDefaultColor()):
    swapColor(board.getTile(start, col), board.getTile(stop, col))
    start -= 1
    stop -= 1
