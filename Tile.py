from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class Tile(QPushButton):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.display()

    def set(self, color):
        self.color = color
        self.display()

    def get(self):
        return self.color

    def display(self):
        self.setStyleSheet("background-color : " + self.color)
