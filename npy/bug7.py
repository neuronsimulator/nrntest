from neuron import h
from e import e

v1 = h.Vector(5).indgen()
v2 = v1.c #left out () so v2 is a callable for the clone function of v1
v1.resize(10)
print (v2)
print((v2.hname()))
e('print (v2.size())') # should give error instead of size of v1
