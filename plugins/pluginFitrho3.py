#--------------------------------------------------
# 	Revision = $Rev: 20 $
# 	Date = $Date: 2011-08-05 20:42:24 +0200 (Fri, 05 Aug 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from pluginInterfaces import PluginFit, Parameter,leastsqFit
import numpy as np

hbarp = 6.626068*10**-34/(2*np.pi);
mass = 133*1.66050*10**-27;
a0= 0.529177*10**-10;
kb = 1.3806504*10**-23;

class PluginFitRho3(PluginFit):
    def __init__(self):
      pass
    
    def fit(self,data,errarray,param,xmin=0,xmax=0, fitAxes=[]):
      """return the data that is needed for plotting the fitting result"""
      self.params = [Parameter(v) for v in param]     
      def f(x):
          return ((2*mass/(np.sqrt(3)*hbarp)*self.params[0]()*3*hbarp*(x**4)*(a0**4)/mass * (4590*np.sinh(2*self.params[2]())/(np.sin(1.0064*np.log(x/self.params[1]()))**2 + np.sinh(self.params[2]())**2)))**0.25) / a0

      minusRegion = data[:,(data[0,:]<0)]
      self.simpleFitAllAxes(f,minusRegion,errarray,xmin,xmax, fitAxes)
      
      return self.generateDataFromParameters(f,[np.amin(minusRegion[0,:]),np.amax(minusRegion[0,:])], np.size(minusRegion[0,:]),xmin,xmax, fitAxes)
      
    def getInitialParameters(self,data):
      """find the best initial values and return them"""
      
      #nothing todo for a linear fit
      return [1,-955,0.08]
      
    def getParameters(self):
      """return the fit parameters"""
      return np.array(["amp","am", "em"])
            
    def getFitModelStr(self):
      """return a string of the implemented fitting model, i.e. 'linear fit (y=A*x +B)'"""
      return "Rho3"
      
    def getResultStr(self):
      """return a special result, i.e. 'Frequency = blabla'"""
      return "nothing fitted"
