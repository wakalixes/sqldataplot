#--------------------------------------------------
# 	Revision = $Rev: 13 $
# 	Date = $Date: 2011-07-31 00:39:24 +0200 (Sun, 31 Jul 2011) $
# 	Author = $Author: stefan $
#--------------------------------------------------

from uncertainties import ufloat, nominal_value, std_dev
from sympy import *

#class vefloat():
#  value = float
#  error = float
#  
#  def __init__(self, value=0.,error=0.):
#     self.value = value
#     self.error = abs(error)
#     
#  def __str__(self):
#    return "%g+-%g" % (self.value, self.error)
#  
#  def __repr__(self):
#    return "vefloat(%s, %s)" % (self.value, self.error)
#  
#  def __float__(self):
#    return self.value
def gaussian_error(term, *errors):
    return sqrt(reduce(Add, (
        (term.diff(var)*Symbol("sigma_"+var.name))**2
        for var in term.atoms(Symbol) if var.name in errors), 0.)) 


def gaussian_error_ufloat(term, **vars):
    st =  gaussian_error(term, *vars.keys())

    subs = {}
    for k,v in vars.iteritems():
        subs[Symbol(k)] = nominal_value(v)
        subs[Symbol("sigma_"+k)] = std_dev(v)

    return ufloat((term.subs(subs),st.n(subs=subs, maxprec=10)))


if __name__ == "__main__":
  fx = ufloat((1,.5))
  fy = ufloat((4,.5))
  
  print "error propagation analytically"
  x,y = symbols("xy")
  at = (x**2+y**2)/(x*y)
  
  print gaussian_error(at, "x", "y")
  print gaussian_error_ufloat(at, x=fx, y=fy)
  
  print "error propagation numerically"
  nt = (fx**2+fy**2)/(fx*fy)
  print nt