import neuron
h = neuron.h

h('demo(2)')

allsec = []
h('forall nrnpython("allsec.append(h.cas())")')

for sec in allsec :
  print(( "%s %d %g"%(sec.name(), sec.nseg, sec(.5).v )))

for sec in h.allsec() :
  print(( "%s %d %g"%(sec.name(), sec.nseg, sec(.5).v )))
