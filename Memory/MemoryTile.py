from BaseGame.Tile import Tile


class MemoryTile(Tile):
    def __init__(self, color, back_color, row, col, callback: callable = print):
        super().__init__(color, row, col, callback)
        self.back_color = back_color
        self.color = color
        self.connect = True
        self.face_down = True

    # set the back color of the tile
    def set_back_color(self, color):
        self.back_color = color

    # get back color of tile
    def get_back_color(self):
        return self.back_color

    # swap the back and front colors to display
    def flip(self):
        temp = self.back_color
        self.back_color = self.color
        self.color = temp
        self.display()

    # determine if another tile matches this one
    def match(self, other_tile):
        if self.color == other_tile.color:
            return True
        else:
            return False