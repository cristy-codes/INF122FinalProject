from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Board(QGridLayout):
    def __init__(self, rows, cols):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.colors = ["black", "cyan", "green", "red", "yellow", "magenta", "blue", "gray"]

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_colors(self):
        return self.colors