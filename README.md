# PyUtils
Included are a bunch of useful python utilities that can be used for various other projects

MasterDataModel.py models the behavour of a Dialog that contains 1 selector widget, a groupBox containing edit controls, and an array of buttons for manipulating objects. Controls are enabled and disabled based on the state of the form. This behaviour can be added to an existing dialog in a single line of code

MasterData Files: 
===================================================
MasterDataDialog.PNG - an example of the type of Dialog that is used

ManageCustomers.py - file generated using Qt Designer and convertedto Python code using pyuic5

ManageCustomersModel.py - file that consumes the ManageCustomers.py code. This is an example of how to use MasterDataModel

MasterDataModel.py - called by ManageCustomersModel to manage the behaviour of objects in relation to the current state of the form, either {INIT,ADD,EDIT}



