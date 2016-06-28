from neuron import h
import numpy
from neuron import nonvint_block_supervisor as nbs
from numpy import exp

h.load_file('nrngui.hoc')

'''
test by adding nonvint_block version of the hh k channel in the presence
of hh with gkbar=0. Should get same AP.
We will not add the k current to the total potassium current so it will be
missing in ik.
'''

class kchan():
  def __init__(self, sectionlist=None):
    if sectionlist:
      self.sl = sectionlist
    else:
      self.sl = h.SectionList()
      for sec in h.allsec():
        self.sl.append()
    self.call = [self.setup, self.initialize,
      self.current, self.conductance, self.fixed_step_solve,
      self.ode_count, self.ode_reinit, self.ode_fun, self.ode_solve, None,
      None
    ]
    self.gkbar = .036
    nbs.register(self.call)

  def __del__(self):
    nbs.unregister(self.call)

  def setup(self):
    size = 0
    for sec in self.sl:
      for seg in sec:
        size += 1
    self.pv = h.PtrVector(size)
    self.hv = h.Vector(size)
    self.v = self.hv.as_numpy()
    self.nodeindices = numpy.empty(size, dtype=int)
    self.n = numpy.empty(size, dtype=float)
    self.g = numpy.empty(size, dtype=float)
    i=0
    for sec in self.sl:
      for seg in sec:
        self.pv.pset(i, seg._ref_v)
        self.nodeindices[i] = seg.node_index()
        i += 1
    #print "setup ", self.nodeindex

  def initialize(self):
    self.pv.gather(self.hv)
    self.n, x = self.ninftau(self.v)
    #print "initialize v=%g n=%g"% (self.seg.v, self.n)

  def current(self, rhs):
    #print "enter current ", rhs
    self.pv.gather(self.hv)
    v = self.v
    n = self.n
    self.g = self.gkbar*n*n*n*n
    i = self.g*(v + 77.)
    rhs[self.nodeindices] -= i
    #print "leave current ", rhs

  def conductance(self, d):
    #print "enter conductance ", d
    d[self.nodeindices] += self.g
    #print "leave conductane ", d, rhs

  def fixed_step_solve(self, dt):
    self.pv.gather(self.hv)
    n = self.n
    ninf, ninv = self.ninftau(self.v)
    self.n += (1. - exp(-dt*ninv))*(ninf - n)
    #print 'fixed step solve dt=%g v=%g ninf=%g n=%g leave n=%g\n'%(dt, v, ninv, n, self.n)

  def ode_count(self, offset):
    #print 'ode_count offset ', offset
    self.offset = offset
    return len(self.v)

  def ode_reinit(self, y):
    y[self.offset:self.offset+len(self.n)] = self.n

  def ode_fun(self, t, y, ydot): # from y determine ydot (if ydot is not None)
    last = self.offset + len(self.n)
    self.pv.gather(self.hv)
    self.n = y[self.offset:last]
    #print "ode_fun t=%g v=%g n=%g"%(h.t, v, self.n)
    if ydot == None:
      return
    ninf, ninv = self.ninftau(self.v)
    ydot[self.offset:last] = (ninf - self.n)*ninv

  def ode_solve(self, dt, t, b, y): #solve mx=b replace b with x (y available if m depends on it
    last = self.offset + len(self.n)
    self.pv.gather(self.hv)
    x,ninv = self.ninftau(self.v)
    b[self.offset:last] /= 1. + dt*ninv
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
    return x/(exp(x) - 1.)
    #return numpy.piecewise(x, [x > 1e-6 or x < -1e-6], \
    #  [lambda x: x / (exp(x) - 1.) , lambda x: 1. - x/2.])

def mk():
  global s, stim
  s = h.Section()
  s.nseg = 10000
  s.diam = 1
  s.L = 20000
  s.insert('hh')
  h.usetable_hh = 0
  stim = h.IClamp(s(0))
  stim.delay = 0.5
  stim.dur = 0.1
  stim.amp = 3
mk()

h.load_file("temp.ses")

def prun():
  xx = h.startsw()
  h.run()
  print h.startsw() - xx

prun()

s.gkbar_hh = 0
k = kchan()
prun()
