from neuron import h
h('create soma')
s = h.IClamp(.5)
seg = s.get_segment()
print seg.sec.name(), seg.x
h.delete_section()
seg = s.get_segment()
print seg

d = h.Section(name='dend')
d.nseg=5
s = h.IClamp(.9, sec=d)
seg = s.get_segment()
print d, seg.sec, seg.sec.name(), seg.x
