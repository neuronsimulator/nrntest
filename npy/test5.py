# assign and evaluate v, diam, cm
from neuron import *
s = h.Section()
s.nseg = 5
s.cm = 2
print(s(.1).cm == 2)
for seg in s:
  seg.v = 10*seg.x
print(s.v == 5)
def a(s):
  print(h.area(.1, sec=s) == h.PI*s.diam*s.L/s.nseg)

a(s)
s.L = 10
a(s)
s.diam=1
a(s)

