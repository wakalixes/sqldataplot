#--------------------------------------------------
# 	Revision = $Rev: 15 $
# 	Date = $Date: 2011-08-01 19:55:53 +0200 (Mon, 01 Aug 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from pluginInterfaces import PluginFit, Parameter,leastsqFit
from pluginConstants import *
import numpy as np

class PluginFitTimeOfFlight(PluginFit):
    def __init__(self):
      pass
    
    def fit(self,array,errarray,param,xmin=0,xmax=0, fitAxes=[]):
      """return the data that is needed for plotting the fitting result"""
      self.params = [Parameter(v) for v in param]
      
      def f(x): return np.sqrt(self.params[0]()**2 + self.params[1]()*CTOFMOL*((x+self.params[2]())**2))
      

      self.simpleFitAllAxes(f,array,errarray,xmin,xmax, fitAxes)
      return self.generateDataFromParameters(f,[np.amin(array[0,:]),np.amax(array[0,:])], np.size(fitAxes)+1, xmin, xmax, fitAxes)
      
    def getInitialParameters(self,data):
      """find the best initial values and return them"""
      
      #nothing todo for a linear fit
      return [0.05,200,8]
      
    def getParameters(self):
      """return the fit parameters"""
      return np.array(["A", "Temp/nK","TOFat(ms)"])
            
    def getFitModelStr(self):
      """return a string of the implemented fitting model, i.e. 'linear fit (y=A*x +B)'"""
      return "TOFmols for offset TOFat y=sqrt(A^2 + CONST*(x+TOFat)^2)"
      
    def getResultStr(self):
      """return a special result, i.e. 'Frequency = blabla'"""
      return "nothing fitted"
