#--------------------------------------------------
# 	Revision = $Rev: 20 $
# 	Date = $Date: 2011-08-05 20:42:24 +0200 (Fri, 05 Aug 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from pluginInterfaces import PluginFit, Parameter,leastsqFit
import numpy as np

class PluginFitExpDec1(PluginFit):
    def __init__(self):
      pass
    
    def fit(self,array,errarray,param,xmin=0,xmax=0,fitAxes=[]):
      """return the data that is needed for plotting the fitting result"""
      self.params = [Parameter(v) for v in param]     
      def f(x): return self.params[0]()*np.exp(-(x)/self.params[1]())
      

      self.simpleFitAllAxes(f,array,errarray,xmin,xmax,fitAxes)
      return self.generateDataFromParameters(f,[np.amin(array[0,:]),np.amax(array[0,:])], np.size(fitAxes)+1, xmin, xmax, fitAxes)
      
    def getInitialParameters(self,data):
      """find the best initial values and return them"""
      """pos = 0"""
      dx = np.abs(data[0,0] - data[0,-1])
      dy = np.abs(data[1,0] - data[1,-1])
      t = dx/10
      mi = np.amin(data[1,:])
      ma = np.amax(data[1,:])
            
      #nothing todo for a linear fit
      return [ma-mi,t]
      
    def getParameters(self):
      """return the fit parameters"""
      return np.array(["A", "t"])
            
    def getFitModelStr(self):
      """return a string of the implemented fitting model, i.e. 'linear fit (y=A*x +B)'"""
      return "Exp. Decay, A*exp(-x/t)"
      
    def getResultStr(self):
      """return a special result, i.e. 'Frequency = blabla'"""
      return "nothing fitted"
