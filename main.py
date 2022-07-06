# Import
import PyQt5.QtWidgets as Qtw
import sys
from GUI.Main_Window import MainWindow

# Run
if __name__ == '__main__':
    app = Qtw.QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec())
