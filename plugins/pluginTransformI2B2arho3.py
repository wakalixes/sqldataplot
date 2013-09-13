#--------------------------------------------------
# 	Revision = $Rev: 20 $
# 	Date = $Date: 2011-08-05 20:42:24 +0200 (Fri, 05 Aug 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from pluginInterfaces import PluginTransform
import numpy as np
from scipy.integrate import odeint
import csv
import os,sys

hbarp = 6.626068*10**-34/(2*np.pi);
mass = 133*1.66050*10**-27;
a0= 0.529177*10**-10;
kb = 1.3806504*10**-23;

class PluginTransformI2B2arho3(PluginTransform):
    def __init__(self):
        self.pathname = os.path.realpath(os.path.dirname(sys.argv[0]))

        def importData(csvFile):
            datacsv = csv.reader(open(self.pathname+"/plugins/feshbachdata/"+csvFile, 'rb'), delimiter=',', quotechar='|')

            data = []
            for row in datacsv:
                try:
                    data.append([float(row[0]), float(row[1])])
                except ValueError:
                    pass
        
            data = np.array(data)
            return data

        self.swaves = importData("swaves.csv")
        self.d0to60 = importData("data0-60.csv")
        self.d490to510 = importData("data490-510.csv")
        self.d540to560 = importData("data540-560.csv")
        self.d750to950 = importData("data750-950.csv")
          
    def transform(self,data, axes, constants):
      def convB2a(bval):
         if bval >= 0 and bval <= 60:
              t = self.d0to60
         elif bval >= 490 and bval <= 510:
              t = self.d490to510
         elif bval >= 540 and bval <= 560:
              t = self.d490to510
         elif bval >= 750 and bval <= 950:
              t = self.d750to950
         else:
              t = self.swaves

         return np.interp(bval, t[:,0], t[:,1])

      def rho3effective(natoms):
          return ((2*mass/(np.sqrt(3)*hbarp)*(8.0*np.sqrt(3.0)*(kb**3)*((NAT**3)-(natoms**3))*(np.pi**3)*(TEMP**3))/((mass**3)*(NAT**2)*(natoms**3)*TIME*(WM**6)))**0.25) / a0
            
       
 #(NN'[t] == -L3Th[B] n3ave[T, wm] *  NN[t]^3)
      A0 = constants[0]
      COILCONVERSION = constants[1]
      FESHBACHRES_CENTER = constants[2]

      TEMP = constants[3]#122*(10**-9)
      WX = constants[4] #6.9
      WY = constants[5]#52.9
      WZ = constants[6]#46.3
      WM = 2*np.pi*(WX*WY*WZ)**(1.0/3.0)
      TIME = constants[7]#0.5

      NAT = np.amax(data[1,:])      
      Bdata = (data[0,:] - A0)*COILCONVERSION + FESHBACHRES_CENTER
      adata = map(convB2a, Bdata) # stores scattering length
      data[0,:] = adata
      data[1,:] = np.array(map(rho3effective,data[1,:]))
      return data

    def getConstants(self):
        return ["A0", "Coil-Conversion", "Feshbach-resonance center", "Temp", "wx","wy","wz","Waiting-Time"]

    def getTransformModelStr(self):
      return "Effective rho3/a0"
    
    def requieredInputParameters(self):
      return None

    def getInfoStr(self):
        return "This plugin uses the equation B = (I-'A0')*'Coil-Conversion'" \
               "+'Freshbarch-resonance center' to convert the current in a coil" \
               " to magnetic-field-strength B. The conversion will touch whatever " \
               "x-axis is selected and will leave all other axes untouched"
