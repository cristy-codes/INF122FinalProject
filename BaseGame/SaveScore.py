from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton


class SaveScore(QDialog):
    def __init__(self, score, game: str):
        super().__init__()

        self.game = game

        self.setWindowTitle("Save Score")
        self.setModal(True)

        self.score = score

        score_label = QLabel(f"Your score: {self.score}")
        score_label.setAlignment(Qt.AlignCenter)

        initials_label = QLabel("Enter your initials (3 letters):")
        self.initials_edit = QLineEdit()
        self.initials_edit.setMaxLength(3)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_score)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)

        button_layout = QHBoxLayout()
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)

        layout = QVBoxLayout()
        layout.addWidget(score_label)
        layout.addWidget(initials_label)
        layout.addWidget(self.initials_edit)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def save_score(self):
        initials = self.initials_edit.text().upper()
        if len(initials) != 3:
            return

        if self.game == "MT":
            with open("memoryScoreboard.txt", "a") as f:
                f.write(f"{self.score} {initials}\n")
        elif self.game == "COL":
            with open("columnsScoreboard.txt", "a") as f:
                f.write(f"{self.score} {initials}\n")

        self.accept()
