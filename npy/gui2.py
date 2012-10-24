from neuron import h
h.load_file("nrngui.hoc")
g = h.Graph()
h.tstop=10
g.size(0,h.tstop,-80,60)
h.graphList[0].append(g)
s = h.Section()
s.insert('hh')
h('objref p')
h('p = new PythonObject()')
g.addexpr('p.s(.5).v - 10')
g.addvar('foo',s(.5)._ref_v)
h.v_init=-70
h.run()

