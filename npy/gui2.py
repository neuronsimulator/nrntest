from neuron import h
h.load_file("nrngui.hoc")
g = h.Graph()
g.size(0,5,-80,60)
h.graphList[0].append(g)
s = h.Section()
h('objref p')
h('p = new PythonObject()')
g.addexpr('p.s(.5).v')
g.addvar('foo',s(.5)._ref_v)
h.run()

