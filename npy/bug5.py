from neuron import h
h('objref p')
h('p = new PythonObject()')
print pow(5,3)
h('print p.pow(5,3)')
print h.p.pow(5,3)

