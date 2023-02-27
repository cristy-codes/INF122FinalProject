from BaseGame.GameConditions import GameConditions

from Memory.MemoryTile import MemoryTile
from Memory.MemoryBoard import MemoryBoard


class MemoryConditions(GameConditions):
    def __init__(self, maxTime):
        super().__init__(maxTime)

    def determineGameOver(self, board: MemoryBoard):
        pass

    def pointSystem(self):
        pass

    def clickEvent(self, tile: MemoryTile, board: MemoryBoard):
        print("Blah")

    def pointSystem(self, board: MemoryBoard):
        pass
