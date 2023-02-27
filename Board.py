from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtCore import QTimer
import random

class Board(QGridLayout):
    def __init__(self, rows=4, cols=4):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.colors = ["black", "cyan", "green", "red", "yellow", "magenta", "blue", "gray"]

        for color in self.colors.copy():
            self.colors.append(color)

        self.buttons = []
        self.clicked_buttons = []
        self.matched_buttons = []

        for i in range(rows):
            for j in range(cols):
                color = random.choice(self.colors)
                self.colors.remove(color)
                button = QPushButton()
                button.setStyleSheet("background-color: white")
                button.clicked.connect(self.button_clicked)
                button.color = color
                self.addWidget(button, i, j)
                self.buttons.append(button)

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def reveal(self):
        for button in self.buttons:
            button.setStyleSheet(f"background-color: {button.color}")
        QTimer.singleShot(1000, self.hide_tiles)

    def hide_tiles(self):
        for button in self.buttons:
            if button not in self.matched_buttons:
                button.setStyleSheet("background-color: white")

    def button_clicked(self):
        button = self.sender()
        if button.color != "white":
            button.setStyleSheet(f"background-color: {button.color}")
            button.setEnabled(False)
            self.clicked_buttons.append(button)
            if len(self.clicked_buttons) == 2:
                if self.clicked_buttons[0].color == self.clicked_buttons[1].color:
                    self.matched_buttons.extend(self.clicked_buttons)
                    self.clicked_buttons = []
                    if len(self.matched_buttons) == len(self.buttons):
                        QMessageBox.information(self.parent(), "Match Tiles Game", "You won!")
                else:
                    QTimer.singleShot(1000, self.hide_clicked_buttons)

    def hide_clicked_buttons(self):
        for button in self.clicked_buttons:
            button.setStyleSheet("background-color: white")
            button.setEnabled(True)
        self.clicked_buttons = []
