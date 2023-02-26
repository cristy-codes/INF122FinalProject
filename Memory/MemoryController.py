from GameController import GameController
from Tile import Tile


class MemoryController(GameController):
    def __init__(self, conditions, turn):
        super().__init__(conditions, turn)

    def handler(self, tile: Tile):
        tile.flip()
        print(tile.getRow(), tile.getCol())
