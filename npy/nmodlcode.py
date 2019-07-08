from neuron import h
for j in range(2):
  mt = h.MechanismType(j)
  name = h.ref("")
  for i in range(mt.count()):
    mt.select(i)
    mt.selected(name)
    a = mt.code().split(sep='\n')
    print("%s : %s" % (name[0], a[0]))

