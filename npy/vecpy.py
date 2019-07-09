import neuron
import time
h = neuron.h

def mytime(s) :
  t = time.time()
  p = eval(s)
  print('%-40s %.3g' % (s, time.time() - t))
  return p

a = mytime('range(0, 1000000)')
v = mytime('h.Vector(a)')
mytime('v.from_python(a)')
print(mytime('v.sum()'))
b = mytime('v.to_python()')
print(len(b))

import sys
sys.path.append('/home/hines/lib64/python')
try:
  import numpy
  a = mytime('numpy.arange(0, 10, .00001)')
  v = mytime('neuron.Vector(a)')
  mytime('v.from_python(a)')
  print(mytime('v.sum()'))
  b = mytime('v.to_python(numpy.zeros(v.size()))')
  print(mytime('b.sum()'))
except:
  print("no numpy")

v = neuron.h.Vector()
mytime('v.from_python(x for x in range(1, 1000000))')
l = mytime('[x for x in v]')

