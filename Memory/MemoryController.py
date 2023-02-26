from BaseGame.GameController import GameController
from BaseGame.Tile import Tile


class MemoryController(GameController):
    def __init__(self, conditions, turn):
        super().__init__(conditions, turn)

    def handler(self, tile: Tile):
        tile.flip()
        print(tile.getRow(), tile.getCol())
