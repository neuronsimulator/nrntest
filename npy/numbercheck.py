from neuron import h
import numpy
from e import e
e('h.abs(numpy.arange(10,11))')
print(h.abs(float(numpy.arange(10,11))))
e('h.abs(0j)')
h('objref p')
h.p = 10 + 2j
print(h.p)

