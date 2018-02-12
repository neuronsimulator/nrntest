from neuron import h
s = h.Section()
s.nseg = 5
s.insert("extracellular")
s.xraxial[0] = 1
s.xraxial[1] = 2
for seg in s:
  seg.xg[0] = seg.x
  seg.xg[1] = 2*seg.x

for seg in s:
  print (seg.xraxial[0], seg.xraxial[1], seg.x, seg.xg[0], seg.xg[1])

