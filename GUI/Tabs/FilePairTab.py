import PyQt5.QtWidgets as Qtw
from GUI.Widgets.Table_Widgets import FileTable
from Processing.Photometry import TableUpdate as TUP
from Processing.Behaviour import TableUpdate as TUB

class FilePairTab(Qtw.QWidget):

    def __init__(self,*args,**kwargs):
        super(FilePairTab,self).__init__(*args, **kwargs)

        self.vlayout = Qtw.QVBoxLayout(self)
        self.setSizePolicy(Qtw.QSizePolicy.MinimumExpanding,Qtw.QSizePolicy.MinimumExpanding)

        self.buttonwid = Qtw.QWidget(self)
        self.buttonhlayout = Qtw.QHBoxLayout(self.buttonwid)
        self.buttonwid.setSizePolicy(Qtw.QSizePolicy.MinimumExpanding,Qtw.QSizePolicy.Fixed)

        self.typewid = Qtw.QWidget(self)
        self.typehlayout = Qtw.QHBoxLayout(self.typewid)
        self.typewid.setSizePolicy(Qtw.QSizePolicy.MinimumExpanding,Qtw.QSizePolicy.Fixed)

        self.table_button_wid = Qtw.QWidget(self)
        self.table_button_layout = Qtw.QHBoxLayout(self.table_button_wid)
        self.table_button_wid.setSizePolicy(Qtw.QSizePolicy.MinimumExpanding,Qtw.QSizePolicy.Fixed)

        #Add Buttons
        self.load_csv_button = Qtw.QPushButton('Load File',self.buttonwid)

        self.save_csv_button = Qtw.QPushButton('Save File',self.buttonwid)

        self.buttonhlayout.addWidget(self.load_csv_button)
        self.buttonhlayout.addWidget(self.save_csv_button)

        #Add File Types

        self.behav_label = Qtw.QLabel('Behavioural Data Type:',self.typewid)

        self.behav_combo = Qtw.QComboBox(self.typewid)
        self.behav_combo.addItems(['','ABET II Raw Data'])

        self.neuraldata_label = Qtw.QLabel('Neural Data Type:',self.typewid)

        self.neuraldata_combo = Qtw.QComboBox(self.typewid)
        self.neuraldata_combo.addItems(['','Doric Photometry Data'])
        self.neuraldata_combo.currentIndexChanged.connect(self.neuraldata_combo_changed)

        self.typehlayout.addWidget(self.behav_label)
        self.typehlayout.addWidget(self.behav_combo)
        self.typehlayout.addWidget(self.neuraldata_label)
        self.typehlayout.addWidget(self.neuraldata_combo)

        # Table Buttons

        self.table_addrow_button = Qtw.QPushButton('Add Row',self.table_button_wid)
        self.table_removerow_button = Qtw.QPushButton('Remove Row',self.table_button_wid)
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

    def neuraldata_combo_changed(self,i):
        self.current_neuraldata = self.neuraldata_combo.currentText()

        if self.current_neuraldata == 'Doric Photometry Data':
            new_col_dict = TUP.table_update(self.current_neuraldata)
            self.filetab.add_cols(num_cols=new_col_dict['num_col'],col_labels = new_col_dict['col_label'],
                                  col_widget=new_col_dict['col_type'],col_spaces=new_col_dict['col_space'])



