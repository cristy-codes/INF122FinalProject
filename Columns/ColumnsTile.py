from BaseGame.Tile import Tile


class ColumnsTile(Tile):
    def __init__(self, color, row, col, callback:callable=print):
        super().__init__(color, row, col, callback)
