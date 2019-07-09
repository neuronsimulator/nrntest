from neuron import h
#without this would get 
# AttributeError: module '__main__' has no attribute 'pow'
from math import pow
h('objref p')
h('p = new PythonObject()')
print((pow(5,3)))
h('print (p.pow(5,3))')
print(h.p.pow(5,3))

