from neuron import h, gui
from math import sin, sqrt
pc = h.ParallelContext()
rank = int(pc.id())
nhost = int(pc.nhost())

h('''
begintemplate Cell
public soma, gid
create soma
proc init() {
  soma {
    nseg=3
    diam = 10
    L = 100/(PI*diam)
    insert pas
    g_pas = .001
    e_pas = -30
  }
}
endtemplate Cell
''')

ncell = 2
cells = {}
for gid in range(rank, ncell, nhost):
  cells[gid] = h.Cell()

imp_ = h.Impedance()
if 0 in cells: imp_.loc(.5, sec=cells[0].soma)

def imp(freq):
  pc.setup_transfer()
  h.finitialize(-65)
  if rank == 0: print ("impedance")
  # all ranks must participate in the compute
  iter = imp_.compute(freq, 1)
  print("freq=%g iter=%g"% (freq, iter))

  for gid in cells:
    print ("cell[%d].soma transfer %g" %(gid, imp_.transfer(.5, sec=cells[gid].soma)))


def run(tstop):
  h.cvode_active(1)
  h.cvode.atol(1e-7)
  h.tstop = tstop
  h.run()
  h.cvode_active(0)


def vec_imp(v, iamp):
  f = v.c().fft(1)
  fa = f.abs()
  imx1 = int(fa.max_ind())
  x1 = f.x[imx1]
  fa.x[imx1] = 0.
  imx2 = int(fa.max_ind())
  x2 = f.x[imx2]
  print ("f[%d]=%g  f[%d]=%g" %(imx1, x1, imx2, x2))
  a = sqrt(x1*x1 + x2*x2)/iamp/(2**(14-1))
  return a

def phenom_imp(freq, iseg, vseg):
  # assumes model is linear and we can run as long as we like
  Dt = 1000/(1024*freq) # 1024 samples per cycle
  v1 = h.Vector()
  v1.record(vseg._ref_v, Dt)
  tstop=20.*1000./freq # run for 20 cycles
  run(tstop) 
  v0 = v1.c()

  stim = h.SinStim(iseg) # i=amp*sin(2*pi*freq*t*(.001)
  stim.freq = freq
  stim.amp = .01
  run(tstop)
  v = v1.c().sub(v0).c(v0.size() - 2**14 - 9, v0.size()-10)
  a = vec_imp(v, stim.amp)
  print ("phenom_imp = %g" % a)
  return v0, v1, v, v.c().fft(1), a

if nhost == 1: imp(0) #should print 1000.0 and 0.0


# add a gap junction

hglist = []

def mkhalfgap(sid, vseg, gapseg, g):
  if vseg != None: pc.source_var(vseg._ref_v, sid, sec=vseg.sec)
  if gapseg != None:
    hg = h.HalfGap(gapseg)
    pc.target_var(hg, hg._ref_vgap, sid)
    hg.g = g
    hglist.append(hg)
    
def mkgap(seg1, seg2, g):
  mkhalfgap(1, seg1, seg2, g)
  mkhalfgap(2, seg2, seg1, g)

def setgap(g):
  for hg in hglist:
    hg.g = g

seg1 = cells[0].soma(.5) if 0 in cells else None
seg2 = cells[1].soma(.5) if 1 in cells else None
mkgap(seg1, seg2, .0001)

for g in [0., .0001, .001, .01]:
  print ("\n gap conductance %g" % g)
  setgap(g)
  imp(0)
  imp(1)
  phenom_imp(1., seg1, seg1)
  phenom_imp(1., seg1, seg2)
  imp(10)
  imp(100)

setgap(0.)
a = phenom_imp(1., seg1, seg1)
gr1 = h.Graph()
a[2].line(gr1)
gr2 = h.Graph()
a[3].line(gr2)

if nhost > 1:
  pc.barrier()
  h.quit()
