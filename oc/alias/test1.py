from neuron import h
h.load_file('test1.hoc')
a = h.A()
h.sf.alias(a, 'test', h._ref_x)
h.a = a

h('print a.test')
h.a.test = 33
print h.a.test
