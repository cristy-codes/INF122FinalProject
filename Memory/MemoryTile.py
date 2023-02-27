from BaseGame.Tile import Tile


class MemoryTile(Tile):
    def __init__(self, color, back_color, row, col, callback: callable = print):
        super().__init__(color, row, col, callback)
        self.back_color = back_color
        self.connect = True

    def set_back_color(self, color):
        self.back_color = color

    def get_back_color(self):
        return self.back_color

    def flip(self):
        temp = self.back_color
        self.back_color = self.color
        self.color = temp
        self.display()

    def disable(self):
        if self.connect:
            self.connect = False
            self.clicked.disconnect()

    def match(self, other_tile):
        if self.color == other_tile.color:
            return True
        else:
            return False

    # Function that occurs on click.
    def call(self, a):
        pass
