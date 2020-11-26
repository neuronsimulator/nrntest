from neuron import h
s = h.Section(name='s')
s.nseg=3
s.insert('pas')

for sec in h.allsec():
  for seg in sec:
    for mech in seg:
      for var in mech:
        print ('%s(%g).%s = %g' % (sec.name(), seg.x, var.name(), var[0]))

