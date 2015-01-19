#--------------------------------------------------
# 	Revision = $Rev: 20 $
# 	Date = $Date: 2011-08-05 20:42:24 +0200 (Fri, 05 Aug 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from plugins.pluginInterfaces import PluginFit
from plugins.pluginInterfaces import PluginFit, Parameter,leastsqFit
from math import exp
import numpy as np

class PluginFitSinus(PluginFit):
    def __init__(self):
      pass
    

    def fit(self,array,errarray,param,xmin=0,xmax=0,fitAxes=[]):
      """return the data that is needed for plotting the fitting result"""
      self.params = [Parameter(v) for v in param]     
      def f(x): return self.params[0]()*np.sin(2*np.pi*x * self.params[1]() - self.params[2]()) + self.params[3]()
      self.simpleFitAllAxes(f,array,errarray,xmin,xmax, fitAxes)
      return self.generateDataFromParameters(f,[np.amin(array[0,:]),np.amax(array[0,:])], np.size(fitAxes)+1, xmin, xmax, fitAxes)
          
    def getParameters(self):
      """return the fit parameters"""
      return np.array(["A", "f/Hz", "phase", "y0"])
    
    def getInitialParameters(self,data):
      """find the best initial values and return them"""
      freq = np.fft.fftfreq(data[0].shape[-1])
      
      sp = np.fft.fft(data[1])
      nd = np.array(list(zip(freq*100000,(sp.real**2 + sp.imag**2))))
      # high pass filter
      nd = nd[2:]
      nd = nd[nd[:,0]>0]
      maxf = np.amax(nd[:,1])
      f = nd[nd[:,1] == maxf][0,0]

      return [np.amax(data[1,:]),f,0,np.mean(data[1,:])]
      
    def getFitModelStr(self):
      """return a string of the implemented fitting model, i.e. 'linear fit (y=A*x +B)'"""
      return "Sinus, A*sin(2*pi*f*x-phase)+y0"
      
    def getResultStr(self):
      """return a special result, i.e. 'Frequency = blabla'"""
      return "nothing fitted"
