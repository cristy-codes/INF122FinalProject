from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from BaseGame.Tile import Tile
from abc import ABC, abstractmethod 

class Board(QGridLayout):
    def __init__(self, rows, cols):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.colors = ["black", "cyan", "green", "red", "yellow", "magenta", "blue", "gray"]
        self.table = [[None for _ in range(cols)] for _ in range(rows)]

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_colors(self):
        return self.colors
    
    def getTile(self, row:int, col:int) -> Tile:
        return self.table[row][col]
    
    # Create all Tile and assign to table
    @abstractmethod
    def setBoard(self):
        # for row in range(self.rows):
        #     for col in range(self.cols):
        #         self.table[row][col] = self.createTile(row, col)
        #         self.addWidget(self.table[row][col], row, col)
        pass

    @abstractmethod
    def createTile(self, row, col, color="white"):
        # return Tile(color, row, col, self.handler)
        pass