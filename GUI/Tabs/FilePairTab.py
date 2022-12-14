import PySide6.QtWidgets as QtWidgets
from GUI.Widgets.Table_Widgets import FileTable
from Processing.Photometry import TableUpdate as TUP
# from Processing.Behaviour import TableUpdate as TUB

class FilePairTab(QtWidgets.QWidget):

    def __init__(self,*args,**kwargs):
        super(FilePairTab,self).__init__(*args, **kwargs)

        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,QtWidgets.QSizePolicy.MinimumExpanding)

        self.buttonwid = QtWidgets.QWidget(self)
        self.buttonhlayout = QtWidgets.QHBoxLayout(self.buttonwid)
        self.buttonwid.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,QtWidgets.QSizePolicy.Fixed)

        self.typewid = QtWidgets.QWidget(self)
        self.typehlayout = QtWidgets.QHBoxLayout(self.typewid)
        self.typewid.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,QtWidgets.QSizePolicy.Fixed)

        self.table_button_wid = QtWidgets.QWidget(self)
        self.table_button_layout = QtWidgets.QHBoxLayout(self.table_button_wid)
        self.table_button_wid.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,QtWidgets.QSizePolicy.Fixed)

        #Add Buttons
        self.load_csv_button = QtWidgets.QPushButton('Load File',self.buttonwid)

        self.save_csv_button = QtWidgets.QPushButton('Save File',self.buttonwid)

        self.buttonhlayout.addWidget(self.load_csv_button)
        self.buttonhlayout.addWidget(self.save_csv_button)

        #Add File Types

        self.behav_label = QtWidgets.QLabel('Behavioural Data Type:',self.typewid)

        self.behav_combo = QtWidgets.QComboBox(self.typewid)
        self.behav_combo.addItems(['','ABET II Raw Data'])

        self.neuraldata_label = QtWidgets.QLabel('Neural Data Type:',self.typewid)

        self.neuraldata_combo = QtWidgets.QComboBox(self.typewid)
        self.neuraldata_combo.addItems(['','Doric Photometry Data'])
        self.neuraldata_combo.currentIndexChanged.connect(self.neuraldata_combo_changed)

        self.typehlayout.addWidget(self.behav_label)
        self.typehlayout.addWidget(self.behav_combo)
        self.typehlayout.addWidget(self.neuraldata_label)
        self.typehlayout.addWidget(self.neuraldata_combo)

        # Table Buttons

        self.table_addrow_button = QtWidgets.QPushButton('Add Row',self.table_button_wid)
        self.table_addrow_button.clicked.connect(self.add_row)
        self.table_removerow_button = QtWidgets.QPushButton('Remove Row',self.table_button_wid)
        self.table_removerow_button.clicked.connect(self.remove_row)
        self.table_button_layout.addWidget(self.table_addrow_button)
        self.table_button_layout.addWidget(self.table_removerow_button)

        # Set V Layout
        self.buttonwid.layout = self.buttonhlayout
        self.typewid.layout = self.typehlayout
        self.vlayout.addWidget(self.buttonwid)
        self.vlayout.addWidget(self.typewid)
        self.vlayout.addWidget(self.table_button_wid)
        self.filetab = FileTable()
        self.vlayout.addWidget(self.filetab)

        self.layout = self.vlayout

    def add_row(self):
        self.filetab.add_row()

    def remove_row(self):
        self.filetab.remove_row()

    def neuraldata_combo_changed(self,i):
        self.current_neuraldata = self.neuraldata_combo.currentText()

        if self.current_neuraldata == 'Doric Photometry Data':
            new_col_dict = TUP.table_update(self.current_neuraldata)
            self.filetab.add_cols(num_cols=new_col_dict['num_col'],col_labels = new_col_dict['col_label'],
                                  col_widget=new_col_dict['col_type'],col_spaces=new_col_dict['col_space'])
        elif self.current_neuraldata == '':
            self.filetab.reset_cols()



