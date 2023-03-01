from Columns.ColumnsConditions import ColumnsConditions
from Columns.ColumnsTurn import ColumnsTurn
from BaseGame.GameController import GameController

"""
ColumnsController class
"""
class ColumnsController(GameController):
  def __init__(self, conditions:ColumnsConditions, columnsTurn:ColumnsTurn):
    #call parent to handle game logic
    super().__init__(conditions, columnsTurn)


  
