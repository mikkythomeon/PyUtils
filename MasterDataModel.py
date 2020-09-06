from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os

#https://stackoverflow.com/questions/23101267/pyqt-qvalidator-function-definition
class FilePathValidator(QtGui.QValidator):
    def __init__(self,parent):
        QtGui.QValidator.__init__(self, parent)
        
    def validate(self,s,pos):
        result = QtGui.QValidator.Acceptable
        if len(s)==0: 
            result = QtGui.QValidator.Intermediate
        elif not os.path.exists(s): result = QtGui.QValidator.Invalid
        return (result,s,pos)
    

class  MasterDataModel():
    def __init__(self, AddButton, SaveButton,CancelButton, DeleteButton,EditGroup, SelectorControl):
        self.AddButton = AddButton
        self.SaveButton = SaveButton
        self.CancelButton = CancelButton
        self.DeleteButton = DeleteButton
        self.EditGroup = EditGroup
        self.SelectorControl = SelectorControl
        self.ActionState = "INIT"
        
        #events section
        #note that the syntax below is only valid in pyQT5!
        self.AddButton.clicked.connect(self.onAddButtonPressed)
        self.CancelButton.clicked.connect(self.onCancelButtonPressed)
        self.SelectorControl.activated.connect(self.onObjectSelected)
        self.DeleteButton.clicked.connect(self.onDeleteButtonPressed)
        self.SaveButton.clicked.connect(self.onSaveButtonPressed)
        
                
        for child in self.EditGroup.findChildren(QtWidgets.QLineEdit):
            print(self.ActionState)
            child.textChanged.connect(self.onFieldDataChanged)
            #add default validation to all the applicable line edits and text 
            #edit controls in the EditControls group. This can always be changed outside of this class later
            regexp = QtCore.QRegExp('^[a-zA-Z0-9]+$')
            validator = QtGui.QRegExpValidator(regexp)
            child.setValidator(validator)        
        self.onInitializeUi()
        
    #https://snorfalorpagus.net/blog/2014/08/09/validating-user-input-in-pyqt4-using-qvalidator/
    def onFieldDataChanged(self, *args, **kwargs):
        #TODO --- optional, error, "sender is not defined"
        #sender = self.sender()
        #validator = sender.validator()
        #state = validator.validate(sender.text(), 0)[0]
        #if state == QtGui.QValidator.Acceptable:
        #    color = '#c4df9b' # green
        #elif state == QtGui.QValidator.Intermediate:
        #    color = '#fff79a' # yellow
        #else:
        #    color = '#f6989d' # red
        #sender.setStyleSheet('QLineEdit { background-color: %s }' % color)
        
        #important link: https://stackoverflow.com/questions/47140550/findchild-on-object-created-within-pyqt-designer
        #This one will drive you crazy because the widgets are not children of the QDialog!!!!
        validcount = 0
        counter = 0
        for child in self.EditGroup.findChildren(QtWidgets.QLineEdit):
            counter+=1
            validator = child.validator()
            if validator!=None:
                state = validator.validate(child.text(), 0)[0] 
                if state==QtGui.QValidator.Acceptable:
                    validcount+=1
        self.SaveButton.setEnabled((validcount==counter) and (self.ActionState!='INIT'))
                        
    def resetAllFields(self):
        for child in self.EditGroup.findChildren(QtWidgets.QLineEdit):
            child.setText('')
                
    def onInitializeUi(self):
        self.resetAllFields()
        self.ActionState='INIT'
        self.DeleteButton.setEnabled(False)
        self.SaveButton.setEnabled(False)
        self.CancelButton.setEnabled(False)
        self.AddButton.setEnabled(True)
        self.SelectorControl.setFocus()
        self.EditGroup.setEnabled(False)
        
    def onAddButtonPressed(self):
        self.resetAllFields()
        self.ActionState='ADD'
        self.DeleteButton.setEnabled(False)
        self.SaveButton.setEnabled(False)
        self.CancelButton.setEnabled(True)
        self.AddButton.setEnabled(False)
        #todo: focus first control                                                      ###
        
        self.EditGroup.setEnabled(True)
        
    def onCancelButtonPressed(self):
        self.onInitializeUi()

    def onObjectSelected(self):
        self.ActionState='EDIT'
        self.DeleteButton.setEnabled(True)
        self.SaveButton.setEnabled(False)
        self.CancelButton.setEnabled(False)
        self.AddButton.setEnabled(True)
        self.EditGroup.setEnabled(True)
                
    def onDeleteButtonPressed(self):
        print ("onDeleteButtonPressed")
        self.ActionState='INIT'
    
    def onSaveButtonPressed(self):
        print ("onSaveButtonPressed")
        self.onInitializeUi()
