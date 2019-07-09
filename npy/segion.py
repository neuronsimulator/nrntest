from neuron import h

s = h.Section(name="soma")
s.insert("hh")
print((dir(s(.5).na_ion)))
print((s(.5).ena))
print((s(.5).na_ion.ena))

evec = h.Vector()
evec.record(s(.5).na_ion._ref_ena, sec=s)

