# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base/file/Ui_importproject.ui'
#
# Created: Sun Oct 27 11:16:54 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ImportProject(object):
    def setupUi(self, ImportProject):
        ImportProject.setObjectName(_fromUtf8("ImportProject"))
        ImportProject.resize(446, 525)
        self.gridLayout = QtGui.QGridLayout(ImportProject)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(ImportProject)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lineEditInputFile = QtGui.QLineEdit(self.groupBox)
        self.lineEditInputFile.setObjectName(_fromUtf8("lineEditInputFile"))
        self.gridLayout_4.addWidget(self.lineEditInputFile, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(0, 27))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.btnBrowsInputFile = QtGui.QPushButton(self.groupBox)
        self.btnBrowsInputFile.setObjectName(_fromUtf8("btnBrowsInputFile"))
        self.gridLayout_4.addWidget(self.btnBrowsInputFile, 0, 2, 1, 1)
        self.lineEditIliModelName = QtGui.QLineEdit(self.groupBox)
        self.lineEditIliModelName.setEnabled(False)
        self.lineEditIliModelName.setObjectName(_fromUtf8("lineEditIliModelName"))
        self.gridLayout_4.addWidget(self.lineEditIliModelName, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.lblProjectName = QtGui.QLabel(self.groupBox)
        self.lblProjectName.setMinimumSize(QtCore.QSize(0, 27))
        self.lblProjectName.setObjectName(_fromUtf8("lblProjectName"))
        self.gridLayout_4.addWidget(self.lblProjectName, 2, 0, 1, 1)
        self.lineEditDbSchema = QtGui.QLineEdit(self.groupBox)
        self.lineEditDbSchema.setText(_fromUtf8(""))
        self.lineEditDbSchema.setObjectName(_fromUtf8("lineEditDbSchema"))
        self.gridLayout_4.addWidget(self.lineEditDbSchema, 2, 1, 1, 1)
        self.cmbBoxAppModule = QtGui.QComboBox(self.groupBox)
        self.cmbBoxAppModule.setEnabled(False)
        self.cmbBoxAppModule.setObjectName(_fromUtf8("cmbBoxAppModule"))
        self.gridLayout_4.addWidget(self.cmbBoxAppModule, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)
        self.btnProjectName = QtGui.QPushButton(self.groupBox)
        self.btnProjectName.setEnabled(True)
        self.btnProjectName.setObjectName(_fromUtf8("btnProjectName"))
        self.gridLayout_4.addWidget(self.btnProjectName, 2, 2, 1, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.gridLayout_4.addWidget(self.dateTimeEdit, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.textEditImportOutput = QtGui.QPlainTextEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEditImportOutput.setFont(font)
        self.textEditImportOutput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEditImportOutput.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.textEditImportOutput.setReadOnly(True)
        self.textEditImportOutput.setObjectName(_fromUtf8("textEditImportOutput"))
        self.verticalLayout.addWidget(self.textEditImportOutput)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ImportProject)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ImportProject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ImportProject.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ImportProject.reject)
        QtCore.QMetaObject.connectSlotsByName(ImportProject)

    def retranslateUi(self, ImportProject):
        ImportProject.setWindowTitle(_translate("ImportProject", "Import Project", None))
        self.groupBox.setTitle(_translate("ImportProject", "Import data ", None))
        self.label.setText(_translate("ImportProject", "Input file: ", None))
        self.btnBrowsInputFile.setText(_translate("ImportProject", "Browse", None))
        self.lineEditIliModelName.setText(_translate("ImportProject", "DM01AVCH24D", None))
        self.label_2.setText(_translate("ImportProject", "Ili model name: ", None))
        self.lblProjectName.setText(_translate("ImportProject", "Project name: ", None))
        self.label_6.setText(_translate("ImportProject", "Application module: ", None))
        self.btnProjectName.setText(_translate("ImportProject", "Check", None))
        self.label_3.setText(_translate("ImportProject", "Date: ", None))
        self.label_4.setText(_translate("ImportProject", "Output:", None))

