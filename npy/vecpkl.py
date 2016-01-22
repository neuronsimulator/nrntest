from neuron import h

try:
  import cPickle as pickle
except:
 import pickle

v1 = h.Vector(3).indgen()
v1.printf()
s = pickle.dumps(v1)
v2 = pickle.loads(s)
v2.printf()
print v1.eq(v2) == 1.0
