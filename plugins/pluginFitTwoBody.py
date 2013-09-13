#--------------------------------------------------
# 	Revision = $Rev: 20 $
# 	Date = $Date: 2011-08-05 20:42:24 +0200 (Fri, 05 Aug 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from pluginInterfaces import PluginFit, Parameter,leastsqFit
import numpy as np

class PluginFitThreeBody(PluginFit):
    def __init__(self):
      pass
    
    def fit(self,array,errarray,param,xmin=0,xmax=0, fitAxes=[]):
      """return the data that is needed for plotting the fitting result"""
      """0...N0, 1...alpha, 2...beta"""
      
      self.params = [Parameter(v) for v in param]     
      def f(x): return self.params[0]()*np.exp(-(self.params[1]())*x/1000)/(1+self.params[0]()*self.params[2]()/(self.params[1]())*(1-np.exp(-self.params[1]()*x/1000)))
      

      self.simpleFitAllAxes(f,array,errarray,xmin,xmax, fitAxes)
      return self.generateDataFromParameters(f,[np.amin(array[0,:]),np.amax(array[0,:])], np.size(array[0,:]),xmin,xmax, fitAxes)
      
    def getInitialParameters(self,data):
      """find the best initial values and return them"""
      return [1000000,0.1,5*10**-7]
      
    def getParameters(self):
      """return the fit parameters"""
      return np.array(["N0","alpha","beta"])
            
    def getFitModelStr(self):
      """return a string of the implemented fitting model, i.e. 'linear fit (y=A*x +B)'"""
      return "Twobody-Decay"
      
    def getResultStr(self):
      """return a special result, i.e. 'Frequency = blabla'"""
      return "nothing fitted"
