# use of HocTopLevelInterpreter should always be at the top level regardless
# of what Hoc object context calls into python
# for test, this is imported from hobjcontext.hoc

from neuron import h

h("x = 5")
h("strdef s")
h("objref o")
h.x = 4
h.s = "hello"
h.o = h.List()
print h.x
print h.s
print h.o.hname()

h("double y[3]")
h("objref oo[2]")
h.y[1] = 25
h.oo[1] = h.Vector()
print h.y[1]
print h.oo[1].hname()

h("func f() { return x*x }")
print h.f()

