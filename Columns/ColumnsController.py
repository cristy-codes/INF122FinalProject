from Columns.ColumnsConditions import ColumnsConditions
from Columns.ColumnsTurn import ColumnsTurn
from BaseGame.GameController import GameController
from PyQt5.QtCore import QTimer, QDateTime


class ColumnsController(GameController):
  def __init__(self, conditions:ColumnsConditions, columnsTurn:ColumnsTurn):
    super().__init__(conditions, columnsTurn)
    self.timer = QTimer()
    self.timer.timeout.connect(self.timerCountdown) # called every second

  # function call every second, subtract by one from maxGameTime
  def timerCountdown(self):
    self.conditions.maxGameTime -= 1
    # sets the label to remaining time left
    self.board.timerLabel.setText('{:02d}:{:02d}'.format(self.conditions.maxGameTime//60,self.conditions.maxGameTime%60))
    # check if there is time remaining
    if (self.conditions.maxGameTime == 0): # time over
      self.stop()

  # added timer start to main start function, to start timer
  def start(self):
    self.timer.start(1000)
    super().start()

  # added timer stop to main stop function, to stop timer
  def stop(self):
    self.timer.stop()
    super().stop()
