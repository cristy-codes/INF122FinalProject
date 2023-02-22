import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from Board import Board


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    grid = Board()

    win.setLayout(grid)
    win.setWindowTitle("122 A4")
    win.setGeometry(50, 50, 200, 200)
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    window()
