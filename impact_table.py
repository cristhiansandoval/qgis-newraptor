from qgis.PyQt.QtWidgets import *
from .impact_table_dialog import Ui_dlgImp

class DlgTable(QDialog, Ui_dlgImp):
    def __init__(self):
        super(DlgTable, self).__init__()
        self.setupUi(self)

        
