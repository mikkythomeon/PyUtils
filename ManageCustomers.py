# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Programming\Python\OrderImport\FileViewerApp\ManageCustomers.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManageCustomersDialog(object):
    def setupUi(self, ManageCustomersDialog):
        ManageCustomersDialog.setObjectName("ManageCustomersDialog")
        ManageCustomersDialog.resize(714, 451)
        self.verticalLayoutWidget = QtWidgets.QWidget(ManageCustomersDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 9, 511, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tvwItems = QtWidgets.QTableView(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tvwItems.sizePolicy().hasHeightForWidth())
        self.tvwItems.setSizePolicy(sizePolicy)
        self.tvwItems.setObjectName("tvwItems")
        self.verticalLayout.addWidget(self.tvwItems)
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 180))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 481, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtCustomerName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtCustomerName.setObjectName("txtCustomerName")
        self.gridLayout.addWidget(self.txtCustomerName, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.txtScriptPath = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtScriptPath.setObjectName("txtScriptPath")
        self.gridLayout.addWidget(self.txtScriptPath, 2, 1, 1, 1)
        self.txtInputPath = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtInputPath.setObjectName("txtInputPath")
        self.gridLayout.addWidget(self.txtInputPath, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.btnScriptPath = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnScriptPath.setObjectName("btnScriptPath")
        self.gridLayout.addWidget(self.btnScriptPath, 2, 3, 1, 1)
        self.btnInputPath = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnInputPath.setObjectName("btnInputPath")
        self.gridLayout.addWidget(self.btnInputPath, 3, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAdd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout_2.addWidget(self.btnAdd)
        self.btnSave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnSave.setEnabled(False)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_2.addWidget(self.btnSave)
        self.btnCancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnCancel.setEnabled(False)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_2.addWidget(self.btnCancel)
        self.btnDelete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnDelete.setEnabled(False)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout_2.addWidget(self.btnDelete)
        self.btnClose = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_2.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ManageCustomersDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(540, 210, 160, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnManageBranches = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnManageBranches.setObjectName("btnManageBranches")
        self.verticalLayout_3.addWidget(self.btnManageBranches)
        self.btnManageSKUs = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnManageSKUs.setObjectName("btnManageSKUs")
        self.verticalLayout_3.addWidget(self.btnManageSKUs)
        self.btnConvertFiles = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnConvertFiles.setObjectName("btnConvertFiles")
        self.verticalLayout_3.addWidget(self.btnConvertFiles)

        self.retranslateUi(ManageCustomersDialog)
        self.btnClose.clicked.connect(ManageCustomersDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ManageCustomersDialog)
        ManageCustomersDialog.setTabOrder(self.tvwItems, self.txtCustomerName)
        ManageCustomersDialog.setTabOrder(self.txtCustomerName, self.txtScriptPath)
        ManageCustomersDialog.setTabOrder(self.txtScriptPath, self.btnScriptPath)
        ManageCustomersDialog.setTabOrder(self.btnScriptPath, self.txtInputPath)
        ManageCustomersDialog.setTabOrder(self.txtInputPath, self.btnInputPath)
        ManageCustomersDialog.setTabOrder(self.btnInputPath, self.btnAdd)
        ManageCustomersDialog.setTabOrder(self.btnAdd, self.btnSave)
        ManageCustomersDialog.setTabOrder(self.btnSave, self.btnCancel)
        ManageCustomersDialog.setTabOrder(self.btnCancel, self.btnDelete)
        ManageCustomersDialog.setTabOrder(self.btnDelete, self.btnClose)

    def retranslateUi(self, ManageCustomersDialog):
        _translate = QtCore.QCoreApplication.translate
        ManageCustomersDialog.setWindowTitle(_translate("ManageCustomersDialog", "Manage Customers"))
        self.groupBox.setTitle(_translate("ManageCustomersDialog", "Customer Data"))
        self.label_4.setText(_translate("ManageCustomersDialog", "Input Filename"))
        self.label_3.setText(_translate("ManageCustomersDialog", "Script Path:"))
        self.label_2.setText(_translate("ManageCustomersDialog", "Customer Name"))
        self.btnScriptPath.setText(_translate("ManageCustomersDialog", "..."))
        self.btnInputPath.setText(_translate("ManageCustomersDialog", "..."))
        self.btnAdd.setText(_translate("ManageCustomersDialog", "Add"))
        self.btnSave.setText(_translate("ManageCustomersDialog", "Save"))
        self.btnCancel.setText(_translate("ManageCustomersDialog", "Cancel"))
        self.btnDelete.setText(_translate("ManageCustomersDialog", "Delete"))
        self.btnClose.setText(_translate("ManageCustomersDialog", "Close"))
        self.btnManageBranches.setText(_translate("ManageCustomersDialog", "Manage Branches"))
        self.btnManageSKUs.setText(_translate("ManageCustomersDialog", "Manage SKUs..."))
        self.btnConvertFiles.setText(_translate("ManageCustomersDialog", "Convert Source Data Files"))
