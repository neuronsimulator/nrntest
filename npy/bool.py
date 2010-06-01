from neuron import h
print [len(h), bool(h)] == [0,True]
o = h.Vector(0)
print [len(o), bool(o)] == [0,False]
o.resize(2)
print [len(o), bool(o)] == [2,True]
o = h.List()
print [len(o), bool(o)] == [0,False]
o.append([])
print [len(o), bool(o)] == [1,True]
h('double a[2][3]')
print [len(h.a), len(h.a[1]), bool(h.a), bool(h.a[1])] == [2,3,True,True]
print [len(h.Vector), bool(h.Vector)] == [0, False]
b = []
for x in range(4) :
  b.append(h.Vector())
print [len(h.Vector), bool(h.Vector)] == [4, True]
b = h.File()
print [len(b), bool(b)] == [0, True]
