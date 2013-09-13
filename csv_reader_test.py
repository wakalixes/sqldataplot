#!/usr/bin/python

from __future__ import with_statement
import numpy as np
import csv as csv
import sys
import os
from PyQt4 import QtCore
from PyQt4 import QtGui
from sdp_ui import Ui_MainWindow
from scipy import linspace, polyval, polyfit, sqrt, stats, randn

path = os.path.dirname(os.path.abspath(sys.argv[0]))
print path
spamReader = csv.reader(open(path+'/data/letztezeile.txt', 'rb'), delimiter='\t', quotechar='|')

arow = [ ]
failsafe = False
for row in spamReader:
  for column,val in enumerate(row):  
    val= val.replace(',','.')
    try:      
	cv = float(val) 
    except ValueError:
      #cv=''
      if column==0:
	 ckey= "dataset:"
	 cv=val
	 keyAt = -1
      elif column==1:
	 ckey= "date:"
	 cv=val+" "+row[column+1]
	 keyAt = 0
      elif column==2:
	 ckey=''
	 keyAt = 1
      else:
	 ckey = val;
	 keyAt = column

    if cv != '' and ckey != '' and column-1 == keyAt:
      arow.append ([ckey,cv])
      print "key: %s val: %s" %(ckey,cv)
      ckey = '' 
      
print arow[3]