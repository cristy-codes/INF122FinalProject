from PyQt5.QtWidgets import QPushButton

"""
Tile class : inherits from QPushButton

@variable color:string - the color of the button
"""
class Tile(QPushButton):
    def __init__(self, color, row, col, callback:callable=print):
        super().__init__()
        self.row = row
        self.col = col
        self.color = color
        self.display()
        self.callback = callback
        self.enable()

    def setColor(self, color):
        self.color = color
        self.display()

    def getColor(self):
        return self.color

    def setRow(self, row):
        self.row = row

    def getRow(self) -> int:
        return self.row
    
    def setCol(self, col):
        self.col = col

    def getCol(self) -> int:
        return self.col

    def disable(self):
        self.clicked.disconnect()

    def enable(self):
        self.clicked.connect(self.click)

    def setCallback(self, callback):
        self.callback = callback

    def getCallback(self) -> callable:
        return self.callback

    def click(self):
        self.callback(self)

    def display(self):
        self.setStyleSheet("background-color : " + self.color)
