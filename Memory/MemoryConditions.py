from BaseGame.GameConditions import GameConditions

from Memory.MemoryTile import MemoryTile
from Memory.MemoryBoard import MemoryBoard


class MemoryConditions(GameConditions):
    def __init__(self, maxTime):
        super().__init__(maxTime)

    # function that determines whether or not the game is still active or over
    def gameOverCondition(self, board: MemoryBoard):
        pass
    
    # calculates points
    def pointSystem(self):
        pass
    
    # idk what this is tbh
    def pointSystem(self, board: MemoryBoard):
        pass

    # establishes what happens when a tile is clicked
    def clickEvent(self, tile: MemoryTile, board: MemoryBoard):
        print("Blah")

    
