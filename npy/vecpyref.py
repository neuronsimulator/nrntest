from neuron import h
import numpy
a = numpy.arange(5.)
print(a)
v = h.Vector(a, 0)
v.printf()

v.x[2] = 25.
v.printf()
print(a)

