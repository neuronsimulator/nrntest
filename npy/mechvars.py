from neuron import h
soma = h.Section(name='soma')
soma.insert('hh')
istim = h.IClamp(soma(.5))
print(dir(soma(.5).hh))
