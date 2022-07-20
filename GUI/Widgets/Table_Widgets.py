# Imports
import PyQt5.QtWidgets as Qtw
import numpy as np
import pandas as pd

# Fil

# File Cell
class FileCell(Qtw.QWidget):

    def __init__(self, parent, row_index, col_index):
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

        self.row_index = row_index
        self.col_index = col_index

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
                                                  'Neural Data File Path'])

        # Add to Layout
        self.filetable.horizontalHeader().resizeSection(0, 300)
        self.filetable.horizontalHeader().resizeSection(1, 300)
        self.filetable.verticalHeader().resizeSection(0, 40)
        self.filetable.setCellWidget(0, 0, FileCell(self, 0, 0))
        self.filetable.setCellWidget(0, 1, FileCell(self, 0, 1))
        self.vlayout.addWidget(self.filetable)
        self.setLayout(self.vlayout)
        self.show()

        # Layout hold values
        self.add_row_widgets = ['FileCell','FileCell']

        # Create data table
        self.filetable_contents = pd.DataFrame(columns=['Behaviour Path', 'Neural Data Path'])

    def add_row(self):
        table_rows = self.filetable.rowCount()
        self.filetable.insertRow(table_rows)

        col_index = 0
        for wid in self.add_row_widgets:
            if wid == 'FileCell':
                self.filetable.setCellWidget(table_rows, col_index, FileCell(self, table_rows, col_index))
            if wid == 'combobox':
                self.filetable.setCellWidget(table_rows, col_index, Qtw.QComboBox())
            col_index += 1

    def remove_row(self):
        table_rows = self.filetable.rowCount()
        self.filetable.removeRow(table_rows - 1)

    def add_cols(self,num_cols,col_labels,col_widget,col_spaces=''):
        self.filetable.setColumnCount((num_cols + 2))
        col_headers = ['Behaviour File Path','Photometry File Path']
        col_headers = col_headers + col_labels
        self.add_row_widgets = self.add_row_widgets + col_widget
        # self.filetable_contents.columns = col_headers
        self.filetable.setHorizontalHeaderLabels(col_headers)
        if col_spaces != '':
            if len(col_spaces) == 1:
                for col in range(2,(2+num_cols)):
                    self.filetable.horizontalHeader().resizeSection(col, col_spaces)
            elif len(col_spaces) == num_cols:
                for col in range(2,(2+num_cols)):
                    index = col-2
                    self.filetable.horizontalHeader().resizeSection(col, col_spaces[index])
        for col in range(2,(2+num_cols)):
            widget_index = col-2
            if col_widget[widget_index] == 'combobox':
                self.filetable.setCellWidget(0,col,Qtw.QComboBox())

