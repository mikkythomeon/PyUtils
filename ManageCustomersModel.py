import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QDialog
from ManageCustomers import Ui_ManageCustomersDialog
from MasterDataModel import *

#Class that manipulates te physical view
class ManageCustomersModel(QDialog):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_ManageCustomersDialog()
        self.ui.setupUi(self)
        self.model = MasterDataModel(self.ui.btnAdd, self.ui.btnSave,self.ui.btnCancel, self.ui.btnDelete, self.ui.groupBox, self.ui.tvwItems)
        
        #wire up the save button to save the data to the database
        #all the validation was taken care of by the MasterDataModel
        self.ui.btnSave.clicked.connect(self.onSave)
        
        #we need to validate that the path names actually exist, so we create a custom validator to validate the paths 
        validator = FilePathValidator(self)
        self.ui.txtScriptPath.setValidator(validator)
        self.ui.txtInputPath.setValidator(validator)
        
    def onSave(self):
        print("save data here")
        
          

if __name__ =="__main__":
    app = QApplication(sys.argv)
    myform = ManageCustomersModel()
    myform.show()
    sys.exit(app.exec_())