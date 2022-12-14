# Import
import PySide6

import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
import sys
from GUI.Main_Window import MainWindow

# Run
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec())
