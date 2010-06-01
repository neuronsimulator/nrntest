from neuron import h
h.load_file('nrngui.hoc')
h.load_file('kschan.ses')
soma = h.Section()
c1 = h.khh(soma(.5))
soma.insert('nahh')
