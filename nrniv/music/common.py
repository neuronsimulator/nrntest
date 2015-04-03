from neuron import h
pc = h.ParallelContext()
nhost = int(pc.nhost())
rank = int(pc.id())

import music

