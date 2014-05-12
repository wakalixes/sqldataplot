#!/usr/bin/python
#--------------------------------------------------
# 	Revision = $Rev: 20 $
# 	Date = $Date: 2011-08-05 20:42:24 +0200 (Fri, 05 Aug 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------
import numpy as np
import os as os
from scipy import optimize
from scipy import odr
def message(s):
    print s
  


from numpy import *

class Parameter:
    isFixed=False
    def __init__(self,value):
        # print "parameter value:",value[0]," fixed=",value[1]
        if not len(value)==2:
            print "Wrong fitting parameter format!"
            return
        self.value=value[0]
        self.isFixed=value[1]
    def set(self, value):
        self.value = value
    def setFixed(self, fix=False):
        self.isFixed=fix
    def __call__(self):
        return self.value

# ToDo: Use curve_fit instead of leastsq
# use weighted least square fit
def curveFit(function, parameters, y, x=None, sigmaIn=None):
    """ warpup of curve_fit
    redefine func() to use only free parameters
    """
    if not x == None:
        x=np.array(x)
    y=np.array(y)
    sigmaIn=np.array(sigmaIn)
    
    # def f(params):
    freeParamIdxs=[i for i,p in enumerate(parameters) if not p.isFixed]  # take only free parameters
    def f(xIn,*fv): # function of freeparamters, f(xIn, FreeParamters)
        for i,v in zip(freeParamIdxs,fv):
            parameters[i].set(v)
        return function(xIn)
    
    if x is None: x = arange(y.shape[0]) # x should be inputted
    freeV0=[] # initial parameters
    for i in freeParamIdxs:
        freeV0.append(parameters[i]())
    freeV0 = np.array(freeV0)
    # print "freeV0: ",freeV0
    # print "sigmain: ",sigmaIn
    # print "x: ",x
    # print "y: ",y
    [popt, pcov]=optimize.curve_fit(f,x,y,p0=freeV0,sigma=sigmaIn,maxfev=500*len(y))
    return [popt, pcov]
  
def leastsqFit(function, parameters, y, x = None):
    """ warpup of leastsq
    used by Stefan in the first version
    """
    # def f(params):
    freeParamIdxs=[i for i,p in enumerate(parameters) if not p.isFixed]  # take only free parameters
    def f(fv): # function of freeparamters
        for i,v in zip(freeParamIdxs,fv):
            parameters[i].set(v)
        return y - function(x)
    
    if x is None: x = arange(y.shape[0]) # x should be inputted
    freeV0=[]
    for i in freeParamIdxs:
        freeV0.append(parameters[i]())
    [out, cov_x, infodict, mesg, resCode] = optimize.leastsq(f, freeV0, full_output=True)  
    return [out, cov_x, infodict, mesg, resCode]

'''
def leastsqFit(function, parameters, y, x = None, fitFixed=[]):
  if fitFixed==[]:
    print "warning: fixed parameters are unsupported"
    fitFixed = [ False for a in parameters]
    
  initparams = [ pv.value for pv in parameters ]
  
  def f(params):
    for i,p in enumerate(parameters):
      p.set(params[i])
'''
      
# METHODE 1: korrektur zur Funktion addieren (siehe fixed ), fehler koennen leider nicht berechnet werden
#    # correction to fix fit parameters
#    corr = 0
#    for i,isFixed in enumerate(fitFixed):
#      v = initparams[i]
#      if isFixed:
#	corr = corr + fixed(v, params[i])
#
#    return y - function(x) + corr
    
# METHODE 2: fixed parameter einfach nicht konvergieren lassen. leider koennen dann auch keine fehler berechnet werden
# fixed parameters, works, but curvature martix is always singular as the fit is not really converging
'''
  def f(params):
    for i,p in enumerate(parameters):
      p.set(params[i] if not fitFixed[i] else initparams[i])

    return y - function(x)


  if x is None: x = arange(y.shape[0])
  p = [param() for param in parameters]

  [out, cov_x, infodict, mesg, resCode] = optimize.leastsq(f, p, full_output=True)  

  return [out, cov_x, infodict, mesg, resCode]
'''
  
def find_subclasses(path, cls):
    """
    Find all subclass of cls in py files located below path
    (does look in sub directories)
 
    @param path: the path to the top level folder to walk
    @type path: str
    @param cls: the base class that all subclasses should inherit from
    @type cls: class
    @rtype: list
    @return: a list if classes that are subclasses of cls
    """
 
    subclasses=[]
 
    def look_for_subclass(modulename):
        #print modulename
        #message("searching %s" % (modulename))
        module=__import__(modulename)
 
        #walk the dictionaries to get to the last one
        d=module.__dict__
        for m in modulename.split('.')[1:]:
            d=d[m].__dict__
 
        #look through this dictionary for things
        #that are subclass of Job
        #but are not Job itself
        for key, entry in d.items():
            if key == cls.__name__:
                continue
 
            try:
                if issubclass(entry, cls):
                   message("Plugin: "+key)
                   subclasses.append(entry)
            except TypeError:
                #this happens when a non-type is passed in to issubclass. We
                #don't care as it can't be a subclass of Job if it isn't a
                #type
                continue
 
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".py") and not name.startswith("__"):
                path = os.path.join(root, name)
                modulename = path.rsplit('.', 1)[0].replace('/', '.')
                look_for_subclass(modulename)
 
    return subclasses

class PluginFit(object):
    # this stores all the results
    curveNum = 0
    fitData = np.array([])
    rerr = np.array([])
    rp = np.array([])
    info = None
    params = ''
    
    def __init__(self):
        pass
        
    def fit(self,array, param, xmin=0, xmax=0, fitAxes=[]):
        """return the data that is needed for plotting the fitting result"""
        return np.array([])      
    
    def getInitialParameters(self,data):
        """find the best initial values and return them"""
        pass
    
    def simpleFitAllAxes(self, f, data, errdata=[], xmin=0, xmax=0, fitAxes=[]):
        """ simple fitting routine, all yaxes get fitted here"""
        # reserve space for results and fit all y axes
        self.curveNum = int(np.size(data,0)-1)
        # print "curveNum:", self.curveNum
        errorcnt = int(np.size(errdata,0))
        self.rp = range(self.curveNum)
        self.rerr = range(self.curveNum)
        self.info = range(self.curveNum)
     
        if not xmin == xmax:
            t = data[:, data[0,:]>xmin]
            data = t[:, t[0,:]<xmax]
            if errorcnt:
                t = errdata[:, data[0,:]>xmin]
                errdata = t[:, t[0,:]<xmax]
            
        # print "ErrorData: ",errdata
        # print "errorcnt: ",errorcnt
        for j in range(self.curveNum):
            if fitAxes[j] and errorcnt==0:
                print "Fitting without error bar ..."
                [out, cov_x, infodict, mesg, resCode]=leastsqFit(f, self.params, data[j+1], data[0])
                freeP = (out)
                # print "covariance: ",cov_x
                if cov_x==None:
                    print "cov_x = None, fitting may be diverged."
                    freeErr=["Err" for i in range(len(freeP))]
                elif (float(len(data[0])) - float(len(out)))<=0:
                    print "# of parameter > Degree of freedom."
                    freeErr=["Err" for i in range(len(freeP))]
                else:
                    freeErr=np.sqrt(np.diag(cov_x)*(infodict['fvec']*infodict['fvec']).sum()/( float(len(data[0])) - float(len(out)) )) # [std_FreeParam1, std_FreeParam2, ...]            
                # Use fitted result(free parameters) to fill self.rp and self.rerr, which are used as parameter outputs
                FreeParamIdx=0
                self.rp[j]=[]
                self.rerr[j]=[]
                for i, p in enumerate(self.params):
                    if p.isFixed:
                        self.rp[j].append(p())
                        self.rerr[j].append(0)
                    else:
                        self.rp[j].append(freeP[FreeParamIdx])
                        self.rerr[j].append(freeErr[FreeParamIdx])
                        FreeParamIdx+=1
                #print type(mesg)
                self.info[j] = 'Fit without error bar.'+str(mesg)

            ### fitting is active, With error bar  
            elif fitAxes[j] and errorcnt>0: # fitting is active, With error bar
                print "Fitting with error bar ..."
                # check if there is an error for every data point
                for i in range(errdata.shape[0]):
                    if errdata[j+1][i]==0:
                        self.info[j] = "At least one data point has an error equal to 0. Try to fit without averaging!"
                        return
                      
                [popt,pcov]=curveFit(f, self.params, y=data[j+1], x=data[0], sigmaIn=errdata[j+1]) # curveFit(function, parameters, y, x=None, sigmaIn=None)
                freeP = (popt) # # [BestValue_FreeParam1, BestValue_FreeParam2, ...]
                # print "fitting out:", popt, pcov
                if pcov==None: #
                    print "pcov = None, fitting may be diverged."
                    freeErr=["Err" for i in range(len(freeP))]
                elif (float(len(data[0])) - float(len(popt)))<=0:
                    print "# of parameter > Degree of freedom."
                    freeErr=["Err" for i in range(len(freeP))]
                else:
                    freeErr= np.sqrt(np.diag(pcov)) # [std_FreeParam1, std_FreeParam2, ...]            
                # Use fitted result(free parameters) to fill self.rp and self.rerr, which are used as parameter outputs
                
                FreeParamIdx=0
                self.rp[j]=[]
                self.rerr[j]=[]
                for i, p in enumerate(self.params):
                    if p.isFixed:
                        self.rp[j].append(p())
                        self.rerr[j].append(0)
                    else:
                        self.rp[j].append(freeP[FreeParamIdx])
                        self.rerr[j].append(freeErr[FreeParamIdx])
                        FreeParamIdx+=1
                #[out, rse]=leastsqFit(f, self.params, data[j+1],data[0])
                #self.rp[j] = (out[0])
                #self.rerr[j]= sqrt(rse*np.diagonal(out[1]))
                self.info[j]="Fit with error bar.\n"
                
            else:
                self.rp[j] = "n/a"
                self.rerr[j]= "n/a"
                self.info[j] = "Nothing selected for fitting."
	
    def generateDataFromParameters(self, f, span, numAxes, xmin=0, xmax=0, fitAxes=[]):
        """ not for public calling, generate data to plot from fit parameters"""
        # fit finished, now lets return the data for plotting a curve of the result
        if xmin == xmax:
            m1=span[0]
            m2=span[1]
        else:
            m1=xmin
            m2=xmax
	
        xdata = np.linspace(m1, m2, 10000)
        fitdata = np.zeros((numAxes, np.size(xdata)))
        fitdata[0,:] = xdata

        #print "fitaxes:", fitAxes
        #print "numaxes:", numAxes
        print "shape rp, fitdata:", len(self.rp), fitdata.shape
        print "rp:",self.rp

        for i,p in enumerate(self.rp):
            if fitAxes[i]:
                for idp,v in enumerate(p):
                    self.params[idp].set(v)
                fitdata[i+1,:] = map(f, fitdata[0,:])
            else:
                fitdata[i+1,:] = None
        return fitdata
      
    def getInfoStr(self):
        return self.info
      
    def getParameters(self):
        """return the fit parameters"""
        return np.array([])
      
    def isConverged(self):
        """return if fitting was good"""
        c = []
        for i in range(0,self.curveNum):
            print self.rp[i]
            if self.rp[i]=="n/a":
                c.append(False)
            else:
                c.append(True)
        return c
      
    def getFitModelStr(self):
        """return a string of the implemented fitting model, i.e. 'linear fit (y=A*x +B)'"""
        return ""
      

class PluginTransform(object):
    def __init__(self):
        pass
        
    def transform(self,data, axes, constants):
        return data
      
    def getTransformModelStr(self):
        return "Identity"
    
    def requieredInputParameters(self):
        return None

    def getConstants(self):
        return None

    def validInputParameters(self,axes):
        neededParameters = self.requieredInputParameters()
        if not neededParameters:
            return True
      
        parameterList = []
        index = -1
        validParameters = 0
        for a in axes:
            index += 1
            if a in neededParameters:
                validParameters += 1
                parameterList.append([a,index])

        if validParameters < len(neededParameters):
            return None

        return dict(parameterList)

    def getInfoStr(self):
        return "This is only an interface"
