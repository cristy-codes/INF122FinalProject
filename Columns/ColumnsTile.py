from BaseGame.Tile import Tile


class ColumnsTile(Tile):
    # defaultColor = "white"
    def __init__(self, row, col, color="white", callback:callable=print):
        # color = color if color else self.getDefaultColor()
        # self.defaultColor = color
        super().__init__(color if color else self.getEmptyTileColor(),
                         row, 
                         col, 
                         callback)

    