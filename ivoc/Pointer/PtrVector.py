from neuron import h
a = h.Vector(5).indgen()
b = h.Vector(5).fill(0)
pv = h.PtrVector(5)
for i in range(len(a)):
  pv.pset(i, b._ref_x[i])

pv.scatter(a)
b.printf()
