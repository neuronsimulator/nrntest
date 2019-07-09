import neuron
h = neuron.h
h('load_file("nrngui.hoc")')
h('create soma')

axon = h.Section()
axon.nseg = 5
axon.L = 1000

sec = axon
soma = h.Section() #not same as hoc soma

for seg in sec:
	print(seg.x)

print(sec, sec.nseg, sec.L)

h('forall psection()')
