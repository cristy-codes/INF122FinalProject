from PyQt5.QtWidgets import QPushButton

"""
Tile class : inherits from QPushButton

@variable color:string - the color of the button
"""
class Tile(QPushButton):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.display()

    def setColor(self, color):
        self.color = color
        self.display()

    def getColor(self):
        return self.color

    def display(self):
        self.setStyleSheet("background-color : " + self.color)
