from neuron import h
soma = h.Section(name='soma')
dend = h.Section(name='dend')
mylist2 = h.SectionList([soma, dend])
sec = dend
del dend
for sec in mylist2:
    print(sec)
