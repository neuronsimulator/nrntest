"""Record Vm using hoc record() syntax and python record syntax()."""

import neuron

h = neuron.h

h('create soma')
h('access soma')
h('insert pas')

stim = h.IClamp(0.5, sec=h.soma)
stim.dur=100
stim.amp=0.1

h('objref vm1')
h('vm1 = new Vector()')
h('vm1.record(&soma.v(0.5))')

vm2 = h.Vector()
vm2.record(h.soma(0.5)._ref_v, sec=h.soma)
ip = h.Vector()
ip.record(h.soma(0.5)._ref_i_pas, sec = h.soma)
pi = h.Vector()
pi.record(h.soma(0.5).pas._ref_i, sec = h.soma)

h.dt = 0.1
neuron.init()
neuron.run(1.0)

print "hoc record() v"
h.vm1.printf()
print "python record() v"
vm2.printf()
print "python record() i_pas"
ip.printf()
print "python record() pas.i"
pi.printf()
