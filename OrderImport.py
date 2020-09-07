import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog

##############################################################################
#   Custom Library Imports
##############################################################################
from MasterDataModel import *
from ManageCustomers import Ui_ManageCustomersDialog
from ManageSKUs import *
from ManageBranches import *

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
        self.ui.btnScriptPath.clicked.connect(self.findScript)
        self.ui.btnInputPath.clicked.connect(self.findInput)
        self.ui.btnManageSKUs.clicked.connect(self.showSKUDIalog)
        self.ui.btnManageBranches.clicked.connect(self.showBranchesDialog)
        
        #we need to validate that the path names actually exist, so we create a custom validator to validate the paths 
        validator = FilePathValidator(self)
        self.ui.txtScriptPath.setValidator(validator)
        self.ui.txtInputPath.setValidator(validator)
        
    def showSKUDIalog(self):
        SKUDialog = ManageSKUsModel(self)
        SKUDialog.show()
    
    def showBranchesDialog(self):
        branchesDialog = ManageBranchesModel(self)
        branchesDialog.show()
    
        
        
    def onSave(self):
        print("save data here")
        
    def findScript(self):
        filename = self.getFileName("Python scripts (*.py)")
        self.ui.txtScriptPath.setText(filename)
        
    def findInput(self):
        filename = self.getFileName("Source files (*.xlsx *.csv)")
        self.ui.txtInputPath.setText(filename)
        
    def getFileName(self, filterString):
        files = QtWidgets.QFileDialog.getOpenFileName(self,"Find File","/",filterString)
        return(files[0])

class ManageSKUsModel(QDialog):
    def __init__(self,parent=None):
        #QtWidgets.QWidget.__init__(self,parent)
        QDialog.__init__(self,parent)
        self.ui = Ui_ManageSKUsDialog()
        self.ui.setupUi(self)
        self.model = MasterDataModel(self.ui.btnAdd, self.ui.btnSave,self.ui.btnCancel, self.ui.btnDelete, self.ui.groupBox, self.ui.tvwItems)
        
        #wire up the save button to save the data to the database
        #all the validation was taken care of by the MasterDataModel
        self.ui.btnSave.clicked.connect(self.onSave)
        
        #we need to validate that the path names actually exist, so we create a custom validator to validate the paths 
        
    def onSave(self):
        print("save data here")
                  

class ManageBranchesModel(QDialog):
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.ui = Ui_ManageBranchesDialog()
        self.ui.setupUi(self)
        self.model = MasterDataModel(self.ui.btnAdd, self.ui.btnSave,self.ui.btnCancel, self.ui.btnDelete, self.ui.groupBox, self.ui.tvwItems)
        
        #wire up the save button to save the data to the database
        #all the validation was taken care of by the MasterDataModel
        self.ui.btnSave.clicked.connect(self.onSave)
        
        #we need to validate that the path names actually exist, so we create a custom validator to validate the paths 
        
    def onSave(self):
        print("save data here")

if __name__ =="__main__":
    app = QApplication(sys.argv)
    customersDialog = ManageCustomersModel()
    customersDialog.show()
    
    #branchesDialog = ManageBranchesModel()
    #branchesDialog.show()
    
    #skusDialog = ManageSKUsModel()
    #skusDialog.show()
    
    sys.exit(app.exec_())