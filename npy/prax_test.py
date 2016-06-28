from neuron import h
v = h.Vector(2)
def efun(v):
  e= (v.x[0]+v.x[1] - 5)**2 + 5*(v.x[0]-v.x[1] - 15)**2
  #print e, v.x[0], v.x[1]
  return e
h.attr_praxis(1e-5, .5, 0)
e = h.fit_praxis(efun, v)
print "e=%g x=%g y=%g\n"%(e, v.x[0], v.x[1])
