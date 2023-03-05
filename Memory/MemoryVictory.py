from PyQt5.QtWidgets import QMessageBox


class MemoryVictory():
    def __init__(self, victoryMessage):
        # set up message box for victory
        msg = QMessageBox()
        msg.setWindowTitle("Victory!")
        msg.setStyleSheet("QLabel{min-width: 100px;}")
        msg.setText(victoryMessage)
        # show the message
        showMessage = msg.exec_()


