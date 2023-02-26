from Tile import Tile


class MemoryTile(Tile):
    def __init__(self, color, back_color):
        super().__init__(color)
        self.back_color = back_color
        self.enable()

    def set_back_color(self, color):
        self.back_color = color

    def get_back_color(self):
        return self.back_color

    def flip(self):
        temp = self.back_color
        self.back_color = self.color
        self.color = temp
        self.display()

    def click(self):
        self.flip()

    def disable(self):
        self.clicked.disconnect()

    def enable(self):
        self.clicked.connect(self.click)

    def match(self, other_tile):
        if self.color == other_tile.color:
            return True
        else:
            return False