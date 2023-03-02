from BaseGame.Tile import Tile


class ColumnsTile(Tile):
    defaultColor = "white"
    
    def __init__(self, row, col, color="white", callback:callable=print):
        # color = color if color else self.getDefaultColor()
        super().__init__(color if color else self.getDefaultColor(),
                         row, 
                         col, 
                         callback)

    def getDefaultColor(self):
        return self.defaultColor

    def setDefaultColor(self):
        self.setColor(self.defaultColor)

    def hasDefaultColor(self):
        return self.getColor() == self.getDefaultColor()
