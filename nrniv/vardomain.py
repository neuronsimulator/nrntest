from neuron import h

h('foo = 2')
h.variable_domain('foo', 1, 5)
h.units('foo', 'cm')

h.xpanel("test")
h.xvalue("foo", "foo", 1)
h.xpvalue("foo", h._ref_foo, 1)
h.xpanel()
