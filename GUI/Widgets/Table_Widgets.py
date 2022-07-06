# Imports
import PyQt5.QtWidgets as Qtw


# File Cell
class FileCell(Qtw.QWidget):

    def __init__(self, parent):
        super(FileCell, self).__init__(parent)

        self.hlayout = Qtw.QHBoxLayout(self)
        self.hlayout.setContentsMargins(5, 0, 5, 0)

        self.text_widget = Qtw.QLineEdit(self)
        self.text_widget.setSizePolicy(Qtw.QSizePolicy.MinimumExpanding, Qtw.QSizePolicy.Fixed)
        self.text_widget.resize(280, 30)

        self.button_widget = Qtw.QPushButton('...', self)
        self.button_widget.clicked.connect(self.set_file_prompt)
        self.button_widget.setSizePolicy(Qtw.QSizePolicy.Fixed, Qtw.QSizePolicy.Fixed)
        self.button_widget.resize(10, 30)

        self.hlayout.addWidget(self.text_widget)
        self.hlayout.addWidget(self.button_widget)

        self.setSizePolicy(Qtw.QSizePolicy.Fixed, Qtw.QSizePolicy.Fixed)

    def set_file_prompt(self):
        file_name = Qtw.QFileDialog.getOpenFileName(self, 'Open File', 'C:\\')
        self.text_widget.setText(str(file_name[0]))

    def get_filepath(self):
        file_string = str(self.text_widget.displayText())
        return file_string


# Table


class FileTable(Qtw.QWidget):

    def __init__(self,*args,**kwargs):
        super(FileTable, self).__init__(*args,**kwargs)

        # Layout #
        self.vlayout = Qtw.QVBoxLayout(self)

        # Table Widget
        self.filetable = Qtw.QTableWidget()
        self.filetable.setRowCount(1)
        self.filetable.setColumnCount(2)
        self.filetable.setHorizontalHeaderLabels(['Behaviour File Path',
                                                  'Photometry File Path'])

        # Add to Layout
        self.filetable.horizontalHeader().resizeSection(0, 300)
        self.filetable.horizontalHeader().resizeSection(1, 300)
        self.filetable.verticalHeader().resizeSection(0, 40)
        self.filetable.setCellWidget(0, 0, FileCell(self))
        self.filetable.setCellWidget(0, 1, FileCell(self))
        self.vlayout.addWidget(self.filetable)
        self.setLayout(self.vlayout)
        self.show()

    def add_row(self):
        table_rows = self.filetable.rowCount()
        self.filetable.insertRow(table_rows)
