# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\asdfz\Downloads\PyLANDrop\filetransferdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileTransferDialog(object):
    def setupUi(self, FileTransferDialog):
        FileTransferDialog.setObjectName("FileTransferDialog")
        FileTransferDialog.resize(400, 66)
        self.verticalLayout = QtWidgets.QVBoxLayout(FileTransferDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.statusLabel = QtWidgets.QLabel(FileTransferDialog)
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)
        self.progressBar = QtWidgets.QProgressBar(FileTransferDialog)
        self.progressBar.setMaximum(10000)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(FileTransferDialog)
        QtCore.QMetaObject.connectSlotsByName(FileTransferDialog)

    def retranslateUi(self, FileTransferDialog):
        _translate = QtCore.QCoreApplication.translate
        FileTransferDialog.setWindowTitle(_translate("FileTransferDialog", "Transferring"))
