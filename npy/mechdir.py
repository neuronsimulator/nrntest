from neuron import h
s = h.Section()
s.insert("hh")
print (dir(s(.5).hh))
