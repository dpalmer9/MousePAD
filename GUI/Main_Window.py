# Imports
import PySide6.QtWidgets as QtWidgets
from GUI.Widgets.Table_Widgets import FileTable
from GUI.Tabs.Window_Tabs import MainTab


# Main GUI

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'MousePAD 0-0-1a'

        self.left = 50
        self.top = 50
        self.width = 800
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.menu = self.menuBar()
        self.filemenu = QtWidgets.QMenu('File',self)
        self.filemenu.addAction('Load Session')
        self.filemenu.addAction('Save Session')
        self.filemenu.addAction('Exit')
        self.menu.addMenu(self.filemenu)
        #self.filetable = FileTable(self)
        #self.filetable.setSizePolicy(QTWidgets.QSizePolicy.MinimumExpanding,QTWidgets.QSizePolicy.Minimum)
        self.maintab = MainTab(self)
        self.setCentralWidget(self.maintab)
        self.show()
