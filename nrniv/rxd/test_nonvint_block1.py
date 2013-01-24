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
    nbs.register(self.call)

  def __del__(self):
    nbs.unregister(self.call)

  def setup(self, unused1, unused2):
    self.nodeindex = 1 #nbs.nodeindex(self.seg)

  def initialize(self, unused1, unused2):
    self.n, x = self.ninftau(self.seg.v)
    #print "initialize v=%g n=%g"% (self.seg.v, self.n)

  def current(self, rhs, unused):
    #print "enter current ", rhs
    v = self.seg.v
    n = self.n
    self.g = 0.036*n*n*n*n
    i = self.g*(v + 77.)
    rhs[self.nodeindex] -= i
    #print "leave current ", rhs

  def conductance(self, d, unused):
    #print "enter conductance ", d
    d[self.nodeindex] += self.g
    #print "leave conductane ", d, rhs

  def fixed_step_solve(self, unused1, unused2):
    v = self.seg.v
    n = self.n
    ninf, ninv = self.ninftau(v)
    dt = h.dt
    self.n += (1. - exp(-dt*ninv))*(ninf - n)
    #print 'fixed step solve v=%g ninf=%g n=%g leave n=%g\n'%(v, ninv, n, self.n)

  def ode_count(self, offset):
    print 'just set offset to', offset
    self.offset = offset
    return 1

  def ode_reinit(self, y, unused):
    y[self.offset] = self.n

  def ode_fun(self, y, ydot): # from y determine ydot
    v = self.seg.v
    self.n = y[self.offset]
    print "ode_fun t=%g v=%g n=%g\n"%(h.t, v, self.n)
    ninf, ninv = self.ninftau(v)
    ydot[self.offset] = (ninf - self.n)*ninv

  def ode_solve(self, b, y): #solve mx=b replace b with x (y available if m depends on it
    v =self.seg.v
    dt = h.dt
    x,ninv = self.ninftau(v)
    b[self.offset] /= 1. + dt*ninv

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

s = h.Section()
s.nseg = 1
s.diam = 10
s.L = 100/(h.PI*s.diam)
s.insert('hh')
s.gkbar_hh = 0
k = kchan(s(.5))
stim = h.IClamp(s(0.5))
stim.delay = 0.5
stim.dur = 0.1
stim.amp = 0.3
h.finitialize(-65)
h.fadvance()

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
