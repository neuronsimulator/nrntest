from neuron import h
import numpy
from neuron import nonvint_block_supervisor as nbs
from math import exp

h.load_file('nrngui.hoc')

'''
test by adding nonvint_block version of the hh k channel in the presence
of hh with gkbar=0. Should get same AP.
We will not add the k current to the total potassium current so it will be
missing in ik.
'''

class kchan():
  def __init__(self, seg):
    self.seg = seg #dangerous as contents can disappear when nseg changes
    self.call = [self.setup, self.initialize,
      self.current, self.conductance, self.fixed_step_solve,
      self.ode_count, self.ode_reinit, self.ode_fun, self.ode_solve ]
    self.gkbar = .036
    nbs.register(self.call)

  def __del__(self):
    nbs.unregister(self.call)

  def setup(self):
    self.nodeindex = 1 #nbs.nodeindex(self.seg)

  def initialize(self):
    self.n, x = self.ninftau(self.seg.v)
    #print "initialize v=%g n=%g"% (self.seg.v, self.n)

  def current(self, rhs):
    #print "enter current ", rhs
    v = self.seg.v
    n = self.n
    self.g = self.gkbar*n*n*n*n
    i = self.g*(v + 77.)
    rhs[self.nodeindex] -= i
    #print "leave current ", rhs

  def conductance(self, d):
    #print "enter conductance ", d
    d[self.nodeindex] += self.g
    #print "leave conductane ", d, rhs

  def fixed_step_solve(self, dt):
    v = self.seg.v
    n = self.n
    ninf, ninv = self.ninftau(v)
    self.n += (1. - exp(-dt*ninv))*(ninf - n)
    #print 'fixed step solve dt=%g v=%g ninf=%g n=%g leave n=%g\n'%(dt, v, ninv, n, self.n)

  def ode_count(self, offset):
    #print 'ode_count offset ', offset
    self.offset = offset
    return 1

  def ode_reinit(self, y):
    y[self.offset] = self.n

  def ode_fun(self, t, y, ydot): # from y determine ydot (if ydot is not None)
    v = self.seg.v
    self.n = y[self.offset]
    #print "ode_fun t=%g v=%g n=%g"%(h.t, v, self.n)
    if ydot == None:
      return
    ninf, ninv = self.ninftau(v)
    ydot[self.offset] = (ninf - self.n)*ninv

  def ode_solve(self, dt, b, y): #solve mx=b replace b with x (y available if m depends on it
    v =self.seg.v
    x,ninv = self.ninftau(v)
    b[self.offset] /= 1. + dt*ninv
    #print 'ode_solve dt=%g'% dt

  def ninftau(self, v):
    na = self.nalpha(v)
    nb = self.nbeta(v)
    ninv = (na + nb)
    return (na/ninv, ninv)

  def nalpha(self, v):
    return 0.01*10.0*self.einstein1(-(v+55.)/10.0)

  def nbeta(self, v):
    return 0.125*exp(-(v+65.)/80.)

  def einstein1(self, x):
    if abs(x) < 1e-6:
      return 1. - x/2.
    else:
      return x/(exp(x) - 1.)

def mk():
  global s, stim
  s = h.Section()
  s.nseg = 1
  s.diam = 10
  s.L = 100/(h.PI*s.diam)
  s.insert('hh')
  h.usetable_hh = 0
  stim = h.IClamp(s(0.5))
  stim.delay = 0.5
  stim.dur = 0.1
  stim.amp = 0.3
mk()

vhh = h.Vector()
vhh.record(s(.5)._ref_v)
h.run()
vhhfixed = vhh.c()
h.cvode_active(1)
h.run()
vhhcvode = vhh.c()

h.cvode_active(0)
s.gkbar_hh = 0
s.nseg=3
s.nseg=1
k = kchan(s(.5))

h.run()
print "mean sq error for fixed step ", vhh.meansqerr(vhhfixed)

h.cvode_active(1)
h.run()
print "trajectory sizes for cvode ", vhhcvode.size(), vhh.size()
s.gkbar_hh = .036
k.gkbar = 0.0
h.run()
print "trajectory sizes for cvode ", vhhcvode.size(), vhh.size()


#h.run()
'''
h.load_file('stdgui.hoc')
print "cvode active"
h.cvode_active(1)
print "cvode step finitialize"
h.finitialize(0)
print "cvode fadvance"
h.fadvance()
'''

h.load_file("temp.ses")
