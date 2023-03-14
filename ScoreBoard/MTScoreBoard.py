import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QLabel

class MTScoreBoard(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 300, 300)
        self.setWindowTitle("Match Tiles Scoreboard")
        self.setModal(True)

        layout = QVBoxLayout()

        with open('memoryScoreboard.txt') as f:
            # read the lines in the file and only show first 10 lines
            lines = f.readlines()[:10]
            # sort the lines by score in descending order
            lines.sort(key=lambda x: int(x.split()[0]), reverse=True)    
            # number the lines
            lines = [f"{i + 1}. {x}" for i, x in enumerate(lines)]
            layout.addWidget(QLabel("\n".join(lines)))
            f.close()

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MTScoreBoard()   
    window.show()
    sys.exit(app.exec())
