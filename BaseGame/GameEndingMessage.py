from PyQt5.QtWidgets import QMessageBox


class GameEndingMessage:
    def __init__(self, message):
        # set up message box for victory
        msg = QMessageBox()
        msg.setWindowTitle("Game over!")
        msg.setStyleSheet("QLabel{min-width: 300px;}")
        msg.setText(message)
        # show the message
        msg.exec_()
