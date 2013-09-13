#--------------------------------------------------
# 	Revision = $Rev: 20 $
# 	Date = $Date: 2011-08-05 20:42:24 +0200 (Fri, 05 Aug 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from pluginInterfaces import PluginTransform
import numpy as np

class PluginTransformI2B(PluginTransform):
    def __init__(self):
      pass
    
    def transform(self,data, axes, constants):
      A0 = constants[0]
      COILCONVERSION = constants[1]
      FESHBACHRES_CENTER = constants[2]
      data[0,:] = (data[0,:] - A0)*COILCONVERSION + FESHBACHRES_CENTER
      return data

    def getConstants(self):
        return ["A0", "Coil-Conversion", "Feshbach-resonance center"]

    def getTransformModelStr(self):
      return "x-axis to B/G"
    
    def requieredInputParameters(self):
      return None

    def getInfoStr(self):
        return "This plugin uses the equation B = (I-'A0')*'Coil-Conversion'" \
               "+'Freshbarch-resonance center' to convert the current in a coil" \
               " to magnetic-field-strength B. The conversion will touch whatever " \
               "x-axis is selected and will leave all other axes untouched"
