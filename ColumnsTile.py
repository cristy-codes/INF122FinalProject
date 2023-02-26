from Tile import Tile

"""
ColumnsTile : inherits from Tile

@variable row:int - row of the tile
@variable col:int - col of the tile
@variable callback:int - function to call for clickEvent
"""
class ColumnsTile(Tile):
    def __init__(self, color, row, col, callback:callable=print):
        super().__init__(color, row, col, callback)

    def getDefaultColor(self):
        return "white"