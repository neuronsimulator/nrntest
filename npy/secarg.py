import neuron
h = neuron.h
h('create soma, dend[3], axon')

import sys
try:
  h.cos(0, sec=3)
except:
  print sys.exc_info()[0], ': ', sys.exc_info()[1]

print h.secname()
print h.secname(sec=h.axon)
print h.secname(sec=h.dend[1])
print h.secname()

print h.cos(0)
print h.cos(0, sec=h.axon)

