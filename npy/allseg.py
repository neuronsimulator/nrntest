from neuron import h
s = h.Section()
s.nseg = 5
for seg in s.allseg():
  print seg.x

h('create axon')
h.axon.nseg=5
for seg in h.axon.allseg():
  print seg.x

