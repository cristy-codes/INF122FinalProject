from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from MemoryTile import MemoryTile
import random


class Board(QGridLayout):
    def __init__(self, rows=4, cols=4):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.colors = ["black", "cyan", "green", "red", "yellow", "magenta", "blue", "gray"]

        for color in self.colors.copy():
            self.colors.append(color)

        for i in range(rows):
            for j in range(cols):
                color = random.choice(self.colors)
                self.colors.remove(color)
                button = MemoryTile("white", color)
                self.addWidget(button, i, j)

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols
