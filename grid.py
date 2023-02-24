import sys
from PyQt5.QtWidgets import QApplication, QDialog

class Grid(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Set grid size')

  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    grid_dialog = Grid()
    grid_dialog.show()

    sys.exit(app.exec())
