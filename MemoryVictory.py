from PyQt5.QtWidgets import QMessageBox


class MemoryVictory():
    def __init__(self, victoryMessage):
        msg = QMessageBox()
        msg.setWindowTitle("Victory!")
        msg.setStyleSheet("QLabel{min-width: 100px;}")
        msg.setText(victoryMessage)
        showMessage = msg.exec_()


