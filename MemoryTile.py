from Tile import Tile
from PyQt5.QtCore import QTimer


class MemoryTile(Tile):
    def __init__(self, color, back_color):
        super().__init__(color)
        self.back_color = back_color
        self.enable()
        self.is_flipped = False
        self.previous_tile = None

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
        if self.is_flipped:
            if self.match(self.previous_tile):
                self.disable()
                self.previous_tile.disable()
            else:
                QTimer.singleShot(1000, lambda: self.flip())
                QTimer.singleShot(1000, lambda: self.previous_tile.flip())
            self.is_flipped = False
            self.previous_tile = None
        else:
            self.is_flipped = True
            self.previous_tile = self

    def disable(self):
        self.clicked.disconnect()

    def enable(self):
        self.clicked.connect(self.click)

    def match(self, other_tile):
        if self.color == other_tile.color:
            return True
        else:
            return False
