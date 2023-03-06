from BaseGame.Tile import Tile


class ColumnsTile(Tile):
    defaultColor = "white"
    
    def __init__(self, row, col, color="white", callback:callable=print):
        # color = color if color else self.getDefaultColor()
        super().__init__(color if color else self.getDefaultColor(),
                         row, 
                         col, 
                         callback)

    # get the default color of the tile
    def getDefaultColor(self):
        return self.defaultColor

    # set the default color of the tile
    def setDefaultColor(self):
        self.setColor(self.defaultColor)

    # determine if the tile has an assigned default color
    def hasDefaultColor(self):
        return self.getColor() == self.getDefaultColor()
