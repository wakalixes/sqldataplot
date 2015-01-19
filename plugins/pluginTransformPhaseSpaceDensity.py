#--------------------------------------------------
# 	Revision = $Rev: 13 $
# 	Date = $Date: 2011-07-31 00:39:24 +0200 (Sun, 31 Jul 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from plugins.pluginInterfaces import PluginTransform
import numpy as np

class PluginTransformPhaseSpaceDensity(PluginTransform):
    def __init__(self):
      pass
    
    def transform(self,data, axes, c):
      ki = self.validInputParameters(axes)
      try:
          ndata = np.ones((2,data[0,:].size))
          ndata[0,:] = data[ki["Tag"],:]
          ndata[1,:] = c[0]**(3/2) * data[ki["Nfit"],:] / (data[ki["width_mum_y"],:]**6)
      except KeyError:
          return None
        
      return ndata
      
    def getTransformModelStr(self):
      return "Phase space density (estimate)"
    
    def requieredInputParameters(self):
      return ["Nfit", "width_mum_y"]

    def getConstants(self):
        return ["Power Dimple2"]

    def getInfoStr(self):
        return "This is a rough estimated for the phase-space density" \
               "the needed input parameters are only the clouds width and " \
               "the atom number"
