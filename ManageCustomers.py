# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Programming\Python\OrderImport\FileViewerApp\ManageCustomers.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_ManageCustomersDialog(QtWidgets.QDialog):
    def setupUi(self, ManageCustomersDialog):
        ManageCustomersDialog.setObjectName("ManageCustomersDialog")
        ManageCustomersDialog.resize(545, 448)
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
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 30, 461, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(19)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtCustomerID = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtCustomerID.setText("")
        self.txtCustomerID.setObjectName("txtCustomerID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtCustomerID)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtCustomerName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtCustomerName.setObjectName("txtCustomerName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtCustomerName)
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

        self.retranslateUi(ManageCustomersDialog)
        self.btnClose.clicked.connect(ManageCustomersDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ManageCustomersDialog)

    def retranslateUi(self, ManageCustomersDialog):
        _translate = QtCore.QCoreApplication.translate
        ManageCustomersDialog.setWindowTitle(_translate("ManageCustomersDialog", "Manage Customers"))
        self.groupBox.setTitle(_translate("ManageCustomersDialog", "Customer Data"))
        self.label.setText(_translate("ManageCustomersDialog", "SAP Customer ID"))
        self.label_2.setText(_translate("ManageCustomersDialog", "Customer Name"))
        self.btnAdd.setText(_translate("ManageCustomersDialog", "Add"))
        self.btnSave.setText(_translate("ManageCustomersDialog", "Save"))
        self.btnCancel.setText(_translate("ManageCustomersDialog", "Cancel"))
        self.btnDelete.setText(_translate("ManageCustomersDialog", "Delete"))
        self.btnClose.setText(_translate("ManageCustomersDialog", "Close"))
