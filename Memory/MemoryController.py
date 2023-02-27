from BaseGame.GameController import GameController
from BaseGame.Tile import Tile

import time

class MemoryController(GameController):
    def __init__(self, conditions, turn):
        super().__init__(conditions, turn)
        self.first_tile = None
        self.second_tile = None

    def handler(self, tile: Tile):
        tile.flip()
        if self.first_tile is None:
            self.first_tile = tile
        elif self.second_tile is None:
            self.second_tile = tile
            if self.first_tile.getColor() == self.second_tile.getColor():
                self.first_tile.disable()
                self.second_tile.disable()
                print("Match")
            else:
                self.first_tile.flip()
                self.second_tile.flip()
            self.first_tile = None
            self.second_tile = None
