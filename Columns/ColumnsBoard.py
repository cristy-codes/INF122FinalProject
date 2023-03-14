from PyQt5.QtWidgets import QLabel, QMessageBox
from Columns.ColumnsTile import ColumnsTile
from PyQt5.QtCore import Qt, QTimer
from BaseGame.Board import Board


class ColumnsBoard(Board):
  def __init__(self, rows, cols, handler=print):
    super().__init__(rows, cols)
    self.handler = handler

    self.colors = ["black", "cyan", "green", "red"]

    self.maxTime = 5

    # set up the board
    self.setBoard()
    # create the timer object
    self.createTimer(self.maxTime, self.timerCountdown)
    # set up the status area
    self.setStatusBar()

  def setStatusBar(self):
    # set up column tile that indicates the next blocks to place
    self.column = [ColumnsTile("white", 0, 0),
                   ColumnsTile("white", 0, 0),
                   ColumnsTile("white", 0, 0)]

    # create label indicating what the next blocks are
    self.queuedBlocksLabel = QLabel("Next block:")
    self.addWidget(self.queuedBlocksLabel, 3, self.cols)

    # add next blocks to board
    self.addWidget(self.column[0], 4, self.cols+1)
    self.addWidget(self.column[1], 5, self.cols+1)
    self.addWidget(self.column[2], 6, self.cols+1)

  ######################################
  def setBoard(self):
    for row in range(self.rows):
      for col in range(self.cols):
        self.table[row][col] = self.createTile(row, col)
        self.addWidget(self.table[row][col], row, col)

  ######################################
  def createTile(self, row, col):
    return ColumnsTile(row, col, None, self.handler)

  ######################################
  # # function call every second
  # def timerCountdown(self):
  #   # sets the label to remaining time left, subtracts time
  #   self.decrementTime()
  #   # check if there is time remaining
  #   if (self.maxTime == 0): # time over
  #     QMessageBox.information(None, "GAME OVER!", "You ran out of time!")
  #     self.timerStop()