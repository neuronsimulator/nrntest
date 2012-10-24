from neuron import h
m = h.Matrix(3,4,2)
m.setval(1,2,100)
m.setval(2,2,200)

def sparse_print(m):
  j = h.ref(0)
  for i in range(int(m.nrow())):
    print i,
    for jx in range(int(m.sprowlen(i))):
      x = m.spgetrowval(i, jx, j)
      print "  %d:%g"%(j[0],x)
    print

sparse_print(m)

