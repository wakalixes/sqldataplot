# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exportDialog.ui'
#
# Created: Thu Jan 15 18:12:26 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_ExportDialog(object):
    def setupUi(self, ExportDialog):
        ExportDialog.setObjectName(_fromUtf8("ExportDialog"))
        ExportDialog.resize(294, 80)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ExportDialog.sizePolicy().hasHeightForWidth())
        ExportDialog.setSizePolicy(sizePolicy)
        self.plotImageCheck = QtGui.QCheckBox(ExportDialog)
        self.plotImageCheck.setGeometry(QtCore.QRect(9, 9, 80, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotImageCheck.sizePolicy().hasHeightForWidth())
        self.plotImageCheck.setSizePolicy(sizePolicy)
        self.plotImageCheck.setMinimumSize(QtCore.QSize(0, 0))
        self.plotImageCheck.setChecked(True)
        self.plotImageCheck.setObjectName(_fromUtf8("plotImageCheck"))
        self.plotDataCheck = QtGui.QCheckBox(ExportDialog)
        self.plotDataCheck.setGeometry(QtCore.QRect(9, 32, 74, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotDataCheck.sizePolicy().hasHeightForWidth())
        self.plotDataCheck.setSizePolicy(sizePolicy)
        self.plotDataCheck.setMinimumSize(QtCore.QSize(0, 0))
        self.plotDataCheck.setChecked(True)
        self.plotDataCheck.setObjectName(_fromUtf8("plotDataCheck"))
        self.buttonBox = QtGui.QDialogButtonBox(ExportDialog)
        self.buttonBox.setGeometry(QtCore.QRect(130, 50, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(ExportDialog)
        QtCore.QMetaObject.connectSlotsByName(ExportDialog)

    def retranslateUi(self, ExportDialog):
        ExportDialog.setWindowTitle(_translate("ExportDialog", "Export options", None))
        self.plotImageCheck.setText(_translate("ExportDialog", "plot (image)", None))
        self.plotDataCheck.setText(_translate("ExportDialog", "plot (data)", None))

