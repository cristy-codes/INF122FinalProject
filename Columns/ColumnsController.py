from Columns.ColumnsConditions import ColumnsConditions
from Columns.ColumnsTurn import ColumnsTurn
from BaseGame.GameController import GameController
from PyQt5.QtCore import QTimer, QDateTime


class ColumnsController(GameController):
  def __init__(self, conditions:ColumnsConditions, columnsTurn:ColumnsTurn):
    super().__init__(conditions, columnsTurn)
    self.timer = QTimer()
    self.timer.timeout.connect(self.timerCountdown) # called every second

  def timerCountdown(self):
    self.conditions.maxGameTime -= 1
    self.board.timerLabel.setText('{:02d}:{:02d}'.format(self.conditions.maxGameTime//60,self.conditions.maxGameTime%60))
    if (self.conditions.maxGameTime == 0): # time over
      self.timer.stop()
      self.stop()

  def start(self):
    self.timer.start(1000)
    super().start()
