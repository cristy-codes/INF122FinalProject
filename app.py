import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from Memory.MemoryGame import MemoryGame
from ScoreBoard.MTScoreBoard import MTScoreBoard
from ScoreBoard.COLScoreBoard import COLScoreBoard
from Columns.ColumnsGame import ColumnsGame

class App(QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        
        # title label
        self.title = QLabel("Select a game:", self)
        self.title.setGeometry(50, 50, 300, 30)
        
        # buttons for each game
        self.mt_button = QPushButton("Match Tiles", self)
        self.mt_button.setGeometry(50, 100, 150, 30)
        self.mt_button.clicked.connect(self.select_mt)
        
        self.col_button = QPushButton("Columns", self)
        self.col_button.setGeometry(50, 150, 150, 30)
        self.col_button.clicked.connect(self.select_col)

        self.score_button = QPushButton("Match Tiles Scoreboard", self)
        self.score_button.setGeometry(50, 200, 150, 30)
        self.score_button.clicked.connect(self.select_mtScore)

        self.score_button = QPushButton("Columns Scoreboard", self)
        self.score_button.setGeometry(50, 250, 150, 30)
        self.score_button.clicked.connect(self.select_colScore)
        
        # status label
        self.status = QLabel("", self)
        self.status.setGeometry(50, 300, 200, 30)

        # Set the window properties
        self.setGeometry(100, 100, 350, 400)
        self.setWindowTitle("Game Selection")
        
    def select_mt(self):
        self.selectedGame = "MT"
        self.status.setText("Match Tiles selected")
        dialog = MemoryGame()
        dialog.show()
        dialog.exec_()
    
    def select_col(self):
        self.selectedGame = "COL"
        self.status.setText("Columns selected")
        dialog = ColumnsGame()
        dialog.show()
        dialog.exec_()

    def select_mtScore(self):
        self.status.setText("View Match Tiles Scores")
        dialog = MTScoreBoard()
        dialog.show()
        dialog.exec_()

    def select_colScore(self):
        self.status.setText("View Columns Scores")
        dialog = COLScoreBoard()
        dialog.show()
        dialog.exec_()
    
def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()