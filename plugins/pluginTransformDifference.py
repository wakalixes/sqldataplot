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
      diff = constants[0]
      data[0,:] = data[0,:] - diff
      return data

    def getConstants(self):
        return ["diff"]

    def getTransformModelStr(self):
      return "x-axis difference"
    
    def requieredInputParameters(self):
      return None

    def getInfoStr(self):
        return "This transform plugin is a mere example, and only returns " \
               "the values of the first axis"
