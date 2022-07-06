import PyQt5.QtWidgets as Qtw
from GUI.Tabs.FilePairTab import FilePairTab

class MainTab(Qtw.QWidget):

    def __init__(self, parent):
        super(MainTab, self).__init__(parent)

        self.layout_type = Qtw.QVBoxLayout(self)

        self.tab_wid = Qtw.QTabWidget()
        self.tab_wid.resize(600, 600)
        self.filetab = FilePairTab()
        self.test = Qtw.QWidget()
        self.test.layout = Qtw.QVBoxLayout(self)
        #self.label = Qtw.QLabel('Test')
        self.test.layout.addWidget(self.filetab)
        self.tab_wid.addTab(self.filetab, "File Pairs")
        self.layout_type.addWidget(self.tab_wid)
        self.setLayout(self.layout_type)
