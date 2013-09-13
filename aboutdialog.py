#--------------------------------------------------
# 	Revision = $Rev: 13 $
# 	Date = $Date: 2011-07-31 00:39:24 +0200 (Sun, 31 Jul 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from PyQt4 import QtCore
from PyQt4 import QtGui
from aboutdialog_ui import Ui_AboutDialog
import csv
import numpy as np

class AboutDialog(QtGui.QMainWindow, Ui_AboutDialog):
  def __init__(self, parent = None):
    super(AboutDialog, self).__init__(parent)
    # setup the GUI --> function generated by pyuic4
    self.parent = parent
    self.setupUi(self)
    QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL('clicked()'),self.close)

# class AboutDialog