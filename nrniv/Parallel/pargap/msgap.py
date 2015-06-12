# combination of multisplit and gap junctions and
# progress statement on just one rank in middle of time step can
# cause deadlock due to some ranks doing parallel transfer and others doing
# spike exchange.

# run this test with 2 ranks

from neuron import h
pc = h.ParallelContext()
rank = int(pc.id())
nhost = int(pc.nhost())
h.load_file("stdrun.hoc")

#two section cell type that can be easily multisplit
h('''

begintemplate Cell
public soma, dend
create soma, dend

proc init() {
  connect dend(0), soma(1)
  soma { L=10  diam= 10 insert hh }
  dend { L=20  diam=1   insert pas  g_pas = .001  e_pas = -65 }
}
endtemplate Cell

''')

# 1 cell for each rank
cell = h.Cell()

# rank 0 cell uses multisplit. Works if rank = 1
if rank == 0:
  h.disconnect(sec=cell.dend)
  pc.multisplit(0.0, rank, sec=cell.dend)
  pc.multisplit(1.0, rank, sec=cell.soma)

# gap junction between soma of rank i and rank (i+1)%nhost
# use sids of 2*i and 2*i + 1 for the source voltages
halfgaps = []
def mkgap(i):
  if rank == i:
    gap = h.HalfGap(cell.soma(.5))
    halfgaps.append(gap)
    pc.source_var(cell.soma(.5)._ref_v, i, sec=cell.soma)
    gap = pc.target_var(gap, gap._ref_vgap, i+1)
  if rank == (i+1)%nhost:
    gap = h.HalfGap(cell.soma(.5))
    halfgaps.append(gap)
    pc.source_var(cell.soma(.5)._ref_v, i+1, sec=cell.soma)
    gap = pc.target_var(gap, gap._ref_vgap, i)

mkgap(0)

def callback():
  print 't=', h.t

def prun():
  pc.timeout(1)
  pc.multisplit()
  pc.set_maxstep(1)
  pc.setup_transfer()
  h.stdinit()
  if rank == 0: h.cvode.event(2.001, callback) #works when 2.0
  pc.psolve(5)

if __name__ == '__main__':
  prun()
  pc.barrier()
  print 0
  h.quit()

