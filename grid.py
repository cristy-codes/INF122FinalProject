import sys
from PyQt6.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QPushButton

class GridDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Set grid size')

        # Create a label and line edit for the number of rows
        rows_label = QLabel('Number of Rows:')
        self.rows_line_edit = QLineEdit()
        rows_layout = QGridLayout()
        rows_layout.addWidget(rows_label, 0, 0)
        rows_layout.addWidget(self.rows_line_edit, 0, 1)

        # Create a label and line edit for the number of columns
        cols_label = QLabel('Number of Columns:')
        self.cols_line_edit = QLineEdit()
        cols_layout = QGridLayout()
        cols_layout.addWidget(cols_label, 0, 0)
        cols_layout.addWidget(self.cols_line_edit, 0, 1)

        # Create a button to submit the grid size
        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.submit_grid_size)

        # Create a grid layout for the dialog
        layout = QGridLayout()
        warning_label = QLabel('Rows and columns must be even numbers')
        layout.addWidget(warning_label, 0, 0)
        layout.addLayout(rows_layout, 1, 0)
        layout.addLayout(cols_layout, 2, 0)
        layout.addWidget(submit_button, 3, 0)

        self.setLayout(layout)

    def submit_grid_size(self):
        rows = int(self.rows_line_edit.text())
        cols = int(self.cols_line_edit.text())

        # Check if the inputs are even numbers
        if rows % 2 != 0 or cols % 2 != 0:
            error_dialog = QDialog()
            error_dialog.setWindowTitle('Error')
            error_label = QLabel('Rows and columns must be even numbers')
            error_layout = QGridLayout()
            error_layout.addWidget(error_label, 0, 0)
            error_dialog.setLayout(error_layout)
            error_dialog.exec()
        else:
            # Create a new dialog to display the grid
            grid_dialog = QDialog()
            grid_dialog.setWindowTitle('Grid')

            # Create a grid layout with the specified number of rows and columns
            grid_layout = QGridLayout()
            for i in range(rows):
                for j in range(cols):
                    label = QLabel(f'({i},{j})')
                    grid_layout.addWidget(label, i, j)

            grid_dialog.setLayout(grid_layout)
            grid_dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    grid_dialog = GridDialog()
    grid_dialog.show()

    sys.exit(app.exec())
