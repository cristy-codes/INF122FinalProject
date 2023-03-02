from BaseGame.Tile import Tile


class ColumnsTile(Tile):
    def __init__(self, row, col, color="white", callback:callable=print):
        # color = color if color else self.getDefaultColor()
        super().__init__(color if color else self.getDefaultColor(),
                         row, 
                         col, 
                         callback)

    def getDefaultColor(self):
        return "white"

    def setDefaultColor(self):
        self.color = "white"

    def hasDefaultColor(self):
        return self.color == self.getDefaultColor()