from neuron import h
h('obfunc newvec() { return new Vector($1) }')
v = h.newvec(10)
v.indgen().add(10)

v.x[-1]
