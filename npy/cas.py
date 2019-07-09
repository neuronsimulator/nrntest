import neuron
h = neuron.h

h('create soma, axon, dend[3]')

print(h.secname())
a = h.axon
a.push() ; print(h.secname())
h.dend[1].push() ; print(h.secname())
h.pop_section()
print(h.secname())
h.pop_section()
print(h.secname())
h.pop_section()
print(h.secname())

a.push()
print(h.secname())
h.pop_section()

a=0
h=0
