from Columns.ColumnsConditions import ColumnsConditions
from Columns.ColumnsTurn import ColumnsTurn
from BaseGame.GameController import GameController


class ColumnsController(GameController):
  def __init__(self, conditions:ColumnsConditions, columnsTurn:ColumnsTurn):
    super().__init__(conditions, columnsTurn)
