from neuron import h
cable = h.Section()
cable.nseg = 5
l = []
for seg in cable:
  print seg.x
  l.append(seg)

for i in l:
  print i, i.x

