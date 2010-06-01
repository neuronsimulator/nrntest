from neuron import h
s = h.Section()
s.insert('hh')
s.insert('extracellular')
s1 = h.IClamp(s(.5))
s2 = h.IClamp(s(.5))
e1 = h.ExpSyn(s(.5))
e2 = h.Exp2Syn(s(.5))
s.rallbranch = 2
print 'rallbranch = ', s.rallbranch
print dir(s)
print dir(s(.5))
print dir(s(.5).hh)

print 'density mechanisms'
for mech in s(.5):
  print mech.name()

print 'point processes'
for p in  s(.5).point_processes():
  print p.hname()
