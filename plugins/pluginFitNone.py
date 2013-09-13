#--------------------------------------------------
# 	Revision = $Rev: 13 $
# 	Date = $Date: 2011-07-31 00:39:24 +0200 (Sun, 31 Jul 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from pluginInterfaces import PluginFit
import numpy as np

class PluginFitNone(PluginFit):
    def __init__(self):
      pass
    
    def fit(self,array,errarray,param,xmin=0,xmax=0, fitAxes=[]):
      """return the data that is needed for plotting the fitting result"""
      return np.array([])
      
    def getParameters(self):
      """return the fit parameters"""
      return []
    
    def getInitialParameters(self,data):
      """find the best initial values and return them"""
      return []
    
    def isConverged(self):
      """return if fitting was good"""
      return True
      
    def getFitModelStr(self):
      """return a string of the implemented fitting model, i.e. 'linear fit (y=A*x +B)'"""
      return "None"
      
    def getResultStr(self):
      """return a special result, i.e. 'Frequency = blabla'"""
      return "nothing fitted"
