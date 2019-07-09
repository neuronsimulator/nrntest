from neuron import h
h("objref ho")

print(h.ho) #1751 segmentation violation

h.ho = None #1751 TypeError: argument must be hoc.HocObject, not None

h.ho = [1,2,3]


