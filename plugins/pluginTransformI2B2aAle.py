#--------------------------------------------------
# 	Revision = $Rev: 20 $
# 	Date = $Date: 2011-08-05 20:42:24 +0200 (Fri, 05 Aug 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from pluginInterfaces import PluginTransform
import numpy as np
import csv
import os,sys

class PluginTransformI2B2a(PluginTransform):
    def __init__(self):
        self.pathname = os.path.realpath(os.path.dirname(sys.argv[0]))

        def importData(csvFile):
            datacsv = csv.reader(open(self.pathname+"/plugins/feshbachdata/"+csvFile, 'rb'), delimiter=',', quotechar='|')

            data = []
            for row in datacsv:
                try:
                    data.append([float(row[0]), float(row[1])])
                except ValueError:
                    pass
        
            data = np.array(data)
            return data

        self.swaves = importData("swaves.csv")
        self.d0to60 = importData("data0-60.csv")
        self.d490to510 = importData("data490-510.csv")
        self.d540to560 = importData("data540-560.csv")
        self.d750to950 = importData("data750-950.csv")
          
    def transform(self,data, axes, constants):
      def convB2a(bval):
         if bval >= 0 and bval <= 60:
              t = self.d0to60
         elif bval >= 490 and bval <= 510:
              t = self.d490to510
         elif bval >= 540 and bval <= 560:
              t = self.d540to560
         elif bval >= 750 and bval <= 950:
              t = self.d750to950
         else:
              t = self.swaves

         return np.interp(bval, t[:,0], t[:,1])

      A0 = constants[0]
      COILCONVERSION = constants[1]
      FESHBACHRES_CENTER = constants[2]
      Bdata = (data[0,:] - A0)*COILCONVERSION + FESHBACHRES_CENTER
      data[0,:] = map(convB2a, Bdata)
      data[1,:] = -data[1,:]
      return data

    def getConstants(self):
        return ["A0", "Coil-Conversion", "Feshbach-resonance center"]

    def getTransformModelStr(self):
      return "x-axis to a/a0 (Ale Style)"
    
    def requieredInputParameters(self):
      return None

    def getInfoStr(self):
        return "This plugin uses the equation B = (I-'A0')*'Coil-Conversion'" \
               "+'Freshbarch-resonance center' to convert the current in a coil" \
               " to magnetic-field-strength B. The conversion will touch whatever " \
               "x-axis is selected and will leave all other axes untouched"
