# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exportDialog.ui'
#
# Created: Fri Jul 08 17:01:21 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

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
        ExportDialog.setWindowTitle(QtGui.QApplication.translate("ExportDialog", "Export options", None, QtGui.QApplication.UnicodeUTF8))
        self.plotImageCheck.setText(QtGui.QApplication.translate("ExportDialog", "plot (image)", None, QtGui.QApplication.UnicodeUTF8))
        self.plotDataCheck.setText(QtGui.QApplication.translate("ExportDialog","plot (data)", None, QtGui.QApplication.UnicodeUTF8))
