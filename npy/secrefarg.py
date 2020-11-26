from neuron import h
soma = h.Section(name='soma')
dend = h.Section(name='dend')
print(soma == h.cas())

sr = h.SectionRef()
print(soma == sr.sec)

sr = h.SectionRef(sec=dend)
print(dend == sr.sec)

sr = h.SectionRef(dend)
print(dend == sr.sec)

print(soma == h.cas())
