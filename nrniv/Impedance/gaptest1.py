from neuron import h
pc = h.ParallelContext()
rank = int(pc.id())
nhost = int(pc.nhost())

h('''
begintemplate Cell
public soma, gid
create soma
proc init() {
  soma {
    nseg=1
    diam = 10
    L = 100/(PI*diam)
    insert pas
    g_pas = .001
    e_pas = -65
  }
}
endtemplate Cell
''')

ncell = 2
cells = {}
for gid in range(rank, ncell, nhost):
  cells[gid] = h.Cell()

imp = h.Impedance()
if 0 in cells: imp.loc(.5, sec=cells[0].soma)

def foo(freq):
  if rank == 0: print("impedance")
  # all ranks must participate in the compute
  imp.compute(freq, 1)

  for gid in cells:
    print("cell[%d].soma transfer %g" %(gid, imp.transfer(.5, sec=cells[gid].soma)))


if nhost == 1: foo(0) #should print 1000.0 and 0.0


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

seg1 = cells[0].soma(.5) if 0 in cells else None
seg2 = cells[1].soma(.5) if 1 in cells else None
mkgap(seg1, seg2, .0001)

pc.setup_transfer()
h.finitialize(-65)

def analytic():
  print('analytic')
  g0 = cells[0].soma(.5).g_pas * cells[0].soma(.5).area() * 0.01
  g1 = cells[1].soma(.5).g_pas * cells[1].soma(.5).area() * 0.01
  ggap = hglist[0].g
  print(g0, ggap, g1)

  r = 1/ggap + 1/g1
  x0 = 1/(g0 + 1/r)
  x1 = x0 * (1/g1 / r)
  print(x0, x1)

foo(0)

if nhost == 1: analytic()

if nhost > 1:
  pc.barrier()
  h.quit()
