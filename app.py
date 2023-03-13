import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from Memory.MemoryGame import MemoryGame
from ScoreBoard.ScoreBoard import ScoreBoard
from Columns.ColumnsGame import ColumnsGame

# Nico - debugging/program execution - remember to remove #
# import hunter
#hunter.trace(action=hunter.CallPrinter)
# Nico - debugging/program execution - remember to remove #

class App(QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        # title label
        self.title = QLabel("Select a game:", self)
        self.title.setGeometry(50, 50, 200, 30)


        # buttons for each game
        self.mt_button = QPushButton("Match Tiles", self)
        self.mt_button.setGeometry(50, 100, 100, 30)
        self.mt_button.clicked.connect(self.select_mt)

        self.col_button = QPushButton("Columns", self)
        self.col_button.setGeometry(50, 150, 100, 30)
        self.col_button.clicked.connect(self.select_col)

        # status label
        self.status = QLabel("", self)
        self.status.setGeometry(50, 250, 200, 30)

        # Set the window properties
        self.setGeometry(100, 100, 300, 300)
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

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
