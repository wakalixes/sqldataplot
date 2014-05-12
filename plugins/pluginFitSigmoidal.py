#--------------------------------------------------
# 	Revision = $Rev: 20 $
# 	Date = $Date: 2011-08-05 20:42:24 +0200 (Fri, 05 Aug 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from pluginInterfaces import PluginFit, Parameter,leastsqFit
import numpy as np

class PluginFitThreeBodyBeta(PluginFit):
    def __init__(self):
      pass
    
    def fit(self,array,errarray,param,xmin=0,xmax=0, fitAxes=[]):
      """return the data that is needed for plotting the fitting result"""
      """0...a, 1...xc, 2...k, 3...y0"""
      
      self.params = [Parameter(v) for v in param]     
      def f(x): return self.params[0]()/(1+np.exp(-(x-self.params[1]())/self.params[2]()))+self.params[3]()
      

      self.simpleFitAllAxes(f,array,errarray,xmin,xmax, fitAxes)
      return self.generateDataFromParameters(f,[np.amin(array[0,:]),np.amax(array[0,:])], np.size(fitAxes)+1, xmin, xmax, fitAxes)
      
    def getInitialParameters(self,data):
      """find the best initial values and return them"""
      dx = np.abs(data[0,0] - data[0,-1])
      mi = np.amin(data[1,:])
      ma = np.amax(data[1,:])
      xc = (np.amax(data[0,:])-np.amin(data[0,:]))/2+np.amin(data[0,:])
      return [ma-mi,xc,dx*2,mi]
      
    def getParameters(self):
      """return the fit parameters"""
      return np.array(["a","xc","dx","y0"])
            
    def getFitModelStr(self):
      """return a string of the implemented fitting model, i.e. 'linear fit (y=A*x +B)'"""
      return "Sigmoidal"
      
    def getResultStr(self):
      """return a special result, i.e. 'Frequency = blabla'"""
      
      return "nothing fitted"
