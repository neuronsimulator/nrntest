from neuron import h
h('objref p, o')
h('p = new PythonObject()')
h('o = p.eval("[1,2,3]")')
print(h.o)

h.nrnpython("a = [1,2,3]")
h.o = h.p.a
h.nrnpython("import hoc")
h.nrnpython("h = hoc.HocObject()")
h.nrnpython("print h.o")

