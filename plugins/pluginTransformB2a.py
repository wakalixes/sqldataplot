#--------------------------------------------------
# 	Revision = $Rev: 13 $
# 	Date = $Date: 2011-07-31 00:39:24 +0200 (Sun, 31 Jul 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from pluginInterfaces import PluginTransform
import numpy as np

class PluginTransformIdentity(PluginTransform):
    def __init__(self):
      pass
    
    def transform(self,data, axes, constants):
      abg = constants[0]
      d = constants[1]
      B0 = constants[2]
      data[0,:] = abg * (1-d/(data[0,:] - B0))
      return data

    def getConstants(self):
        return ["a_bg", "Delta", "B0"]

    def getTransformModelStr(self):
      return "x-axis to a/a0"
    
    def requieredInputParameters(self):
      return None

    def getInfoStr(self):
        return "This transform plugin is a mere example, and only returns " \
               "the values of the first axis"
