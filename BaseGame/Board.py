from PyQt5.QtWidgets import QGridLayout
from BaseGame.Tile import Tile
from abc import abstractmethod 
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QTimer

class Board(QGridLayout):
    def __init__(self, rows, cols):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.colors = ["black", "cyan", "green", "red", "yellow", "magenta", "blue", "gray"]
        self.table = [[None for _ in range(cols)] for _ in range(rows)] # set up blank 2D list that represents the board
        
        # create labels for score and add to display
        self.scoreStatusLabel = QLabel("Score:")
        self.scoreLabel = QLabel("0")
        self.addWidget(self.scoreStatusLabel, 0, self.cols, 2, 1, Qt.Alignment())
        self.addWidget(self.scoreLabel, 0, self.cols+2, 2, 1, Qt.Alignment())
        
    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_colors(self):
        return self.colors
    
    def getTile(self, row:int, col:int) -> Tile:
        return self.table[row][col]

    #### TIMER STUFF START, COULD BE MOVED TO ITS OWN CLASS ####
    # Subtracts time by 1 and updates corresponding label
    def decrementTime(self):
        # subtracts time
        self.maxTime -= 1
        # sets the label to remaining time left
        self.timerLabel.setText('{:02d}:{:02d}'.format(self.maxTime//60, self.maxTime%60))

    # sets up the labels for the timer, and instantiates the timer object itself
    def createTimer(self, maxTime:int, timerCountdown):
        # set up timer labels
        self.timerStatusLabel = QLabel("Time Remaining:")
        self.timerLabel = QLabel("00:00")
        self.addWidget(self.timerStatusLabel, 1, self.cols, 2, 1, Qt.Alignment())
        self.addWidget(self.timerLabel, 1, self.cols + 2, 2, 1, Qt.Alignment())

        self.maxTime = maxTime
        # create timer
        self.timer = QTimer()
        # assign function that will be called every second
        self.timer.timeout.connect(timerCountdown)
        # start timer
        self.timer.start(1000)

    # Function that is called every second (that the timer counts down)
    def timerCountdown(self):
        self.decrementTime()
        # if there is no more time remaining, declare a game loss.
        if self.maxTime == 0:
            self.timer.stop()
    
    #### TIMER STUFF END, COULD BE MOVED TO ITS OWN CLASS ####

    def disableAllTiles(self):
        for tileList in self.table:
            for tile in tileList:
                tile.disable()

    ######################################
    # Create all Tiles and assign to table
    @abstractmethod
    def setBoard(self):
        pass
    
    ######################################
    # Create an individual tile
    @abstractmethod
    def createTile(self, row, col, color="white"):
        pass