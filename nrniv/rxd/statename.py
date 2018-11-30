from kchanarray import kchan
from neuron import h
s = h.Section(name='soma')
s.diam = 10
s.L = 3
s.nseg=1
s.insert('hh')
h.usetable_hh = 0
stim = h.IClamp(s(.5))
stim.delay = 0.5
stim.dur = 0.1
stim.amp = .3

s.gkbar_hh = 0
k = kchan()
h.run()

h.cvode.active(True)
r = h.ref('')
h.finitialize()
states = h.Vector()
h.cvode.states(states)
print("states")
states.printf()

dstates = h.Vector()
print("dstates")
h.cvode.dstates(dstates)
dstates.printf()

print ("statenames")
for i in range(len(states)):
  h.cvode.statename(i,r)
  print (r[0])

