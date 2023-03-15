from PyQt5.QtWidgets import QPushButton

"""
Tile class : inherits from QPushButton

@variable color:string - the color of the button
"""
class Tile(QPushButton):
    emptyTileColor = "white"
    def __init__(self, color, row, col, callback:callable=print):
        super().__init__()
        self.row = row
        self.col = col
        self.color = color
        self.display()
        self.callback = callback
        self.enable()

    # change the color of the tile and display it
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

    # disable button to prevent clicking
    def disable(self):
        self.clicked.disconnect()

    # enable button to enable clicking
    def enable(self):
        self.clicked.connect(self.click)

    # actions that are performed once a tile is clicked
    def click(self):
        self.callback(self)

    # show the tile's color
    def display(self):
        self.setStyleSheet("background-color : " + self.color)

    # mark tile as empty
    def clearTile(self):
        self.setColor(self.emptyTileColor)

    # get the default color of the tile
    def getEmptyTileColor(self):
        return self.emptyTileColor

    # determine if the tile has an assigned default color
    def hasEmptyTileColor(self):
        return self.getColor() == self.getEmptyTileColor()
