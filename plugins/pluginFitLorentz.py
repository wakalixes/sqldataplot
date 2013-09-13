#--------------------------------------------------
# 	Revision = $Rev: 20 $
# 	Date = $Date: 2011-08-05 20:42:24 +0200 (Fri, 05 Aug 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from pluginInterfaces import PluginFit
from pluginInterfaces import PluginFit, Parameter,leastsqFit
from math import exp
import numpy as np

class PluginFitLorentz(PluginFit):
    def __init__(self):
      pass
    

    def fit(self,array,errarray,param,xmin=0,xmax=0, fitAxes=[]):
      """return the data that is needed for plotting the fitting result"""
      self.params = [Parameter(v) for v in param]     
      def f(x):
          #Offset + 2*A/pi * w/(4 (x-pos)^2 + w^2)
          return 2*self.params[0]()/(np.pi) * (self.params[2]() / (4*(x-self.params[1]())**2 + self.params[2]()**2)) + self.params[3]()
      
      self.simpleFitAllAxes(f,array,errarray,xmin,xmax, fitAxes)
      return self.generateDataFromParameters(f,[np.amin(array[0,:]),np.amax(array[0,:])], np.size(array[0,:]),xmin,xmax, fitAxes)
          
    def getParameters(self):
      """return the fit parameters"""
      return np.array(["Amplitude", "Position", "Width", "Offset"])
    
    def getInitialParameters(self,data):
      """find the best initial values and return them"""

      #return [np.amax(data[1,:]),f,0,np.mean(data[1,:]),0]
      x = sum(data[0]*data[1])/sum(data[1])
      width = np.sqrt(abs(sum((data[0]-x)**2*data[1])/sum(data[1])))
      minf = np.amin(data[1])  
      
      return [-(np.amax(data[1,:])-np.amin(data[1,:])), x, width,np.amax(data[1,:])]
      
    def getFitModelStr(self):
      """return a string of the implemented fitting model, i.e. 'linear fit (y=A*x +B)'"""
      return "Lorentz"
      
    def getResultStr(self):
      """return a special result, i.e. 'Frequency = blabla'"""
      return "nothing fitted"
