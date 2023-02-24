from Tile import Tile

"""
ColumnsTile : inherits from Tile

@variable row:int - row of the tile
@variable col:int - col of the tile
@variable callback:int - function to call for clickEvent
"""
class ColumnsTile(Tile):
    def __init__(self, color, row, col, callback:callable=print):
        super().__init__(color)
        self.row = row
        self.col = col
        self.callback = callback
        self.enable()

    def setRow(self, row):
        self.row = row

    def getRow(self) -> int:
        return self.row
    
    def setCol(self, col):
        self.col = col

    def getCol(self) -> int:
        return self.col
    
    def setCallback(self, callback):
        self.callback = callback

    def getCallback(self) -> callable:
        return self.callback

    def click(self):
        self.callback(self)

    def disable(self):
        self.clicked.disconnect()

    def enable(self):
        self.clicked.connect(self.click)
