# Imports
import PyQt5.QtWidgets as Qtw
from GUI.Widgets.Table_Widgets import FileTable
from GUI.Tabs.Window_Tabs import MainTab


# Main GUI

class MainWindow(Qtw.QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'MousePAD 0-0-1a'

        self.left = 50
        self.top = 50
        self.width = 800
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        #self.filetable = FileTable(self)
        #self.filetable.setSizePolicy(Qtw.QSizePolicy.MinimumExpanding,Qtw.QSizePolicy.Minimum)
        self.maintab = MainTab(self)
        self.setCentralWidget(self.maintab)
        self.show()
