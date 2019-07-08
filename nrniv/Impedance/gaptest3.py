# test bugfix where number of halfgap is > number of states.
from neuron import h, gui

# three compartment cable (two zero area compartments)
cab = h.Section(name="cable")
cab.nseg=1
cab.L = 100
cab.diam=5
cab.insert('pas')
cab.g_pas = .001
cab.e_pas = -65
cab.Ra = 100

#impedance
imp = h.Impedance()
imp.loc(0, sec=cab)

ri = [seg.ri() for seg in cab.allseg()]

def foo(s):
  print(s)
  h.stdinit()
  print ("ri ", [seg.ri() for seg in cab.allseg()])
  for freq in [1., 10., 100.]:
    imp.compute(freq, 1, 5000)
    x = [seg.x for seg in cab.allseg()]
    trans = [imp.transfer(i, sec=cab) for i in x]
    print('freq=%g transimped=' % (freq), trans)

foo("nseg=1")
cab.Ra = 1e6
foo("nseg=1 Ra=1e6")

#Mimic ri with gap junctions.

pc = h.ParallelContext()
def mkgaps():
  segs = [seg for seg in cab.allseg()]
  for i, seg in enumerate(segs): # voltage source sids
    pc.source_var(seg._ref_v, i, sec=seg.sec)
  for i in range(1, len(segs)):
    mkgap(i-1, segs[i-1], i, segs[i], 1./ri[i])
  pc.setup_transfer()

def mkgap(sgid1, seg1, sgid2, seg2, g):
  mkhgap(sgid1, seg2, g)
  mkhgap(sgid2, seg1, g)

hglist = []
def mkhgap(sid, seg, g):
  hg = h.HalfGap(seg)
  hg.g = g
  pc.target_var(hg, hg._ref_vgap, sid)
  hglist.append(hg)

mkgaps()
foo("nseg=1 gaps")

hglist = []
pc.gid_clear()
cab.L=1000
cab.Ra = 100
cab.nseg = 3
ri = [seg.ri() for seg in cab.allseg()]
imp.loc(.01, sec=cab)
foo("nseg=3 cable")
cab.Ra = 1e6
mkgaps()
foo("nseg=3 gaps")

