import neuron
h = neuron.h
h.load_file('stdgui.hoc')
soma = h.Section()
v = h.Vector()
soma.insert("hh")
soma.L=10
soma(.5).diam = 3

v.record(soma(.5)._ref_v, sec = soma)

h.run()
v.printf()

