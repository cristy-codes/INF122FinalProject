import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from grid import GridDialog

class GameSelection(QMainWindow):
    def __init__(self, parent=None):
        super(GameSelection, self).__init__(parent)
        
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
        self.status.setGeometry(50, 200, 200, 30)

        # Set the window properties
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("Game Selection")
        
    def select_mt(self):
        self.status.setText("Match Tiles selected")
        dialog = GridDialog()
        dialog.show()
        dialog.exec()
    
    def select_col(self):
        self.status.setText("Columns selected")
        dialog = GridDialog()
        dialog.show()
        dialog.exec()
    
def main():
    app = QApplication(sys.argv)
    window = GameSelection()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()