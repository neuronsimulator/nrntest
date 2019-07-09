import neuron
h = neuron.h

h('create soma, axon, dend[3]')
h.axon.connect(h.soma, 0, 0)
for i in range(3) :
  h.dend[i].connect(h.soma)
h.topology()

h.soma.push() ; sr = h.SectionRef() ; h.pop_section()

for s in sr.child :
  print(s.name())

h('objref sr')
h.sr = sr
h('for i = 0,  sr.nchild-1 sr.child[i] print secname()')

h=0
sr=0
