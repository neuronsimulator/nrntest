# test of the nrn.Section.simulate method

from neuron import h, gui

def pr():
  print(("cache_efficient is %d" %h.cvode.cache_efficient(1)))
  for sec in h.allsec():
    print((sec.name()))
  h.topology()
  h.run()

a = [h.Section(name='s'+str(i)) for i in range(5)]

try:
  h.load_file("nosim.ses")
except:
  pass

h.cvode.active(1)
pp = []
for sec in a:
  sec.L = 10
  sec.diam = 3
  sec.insert("hh")
  pp.append(h.IClamp(sec(.5)))
for i, p in enumerate(pp):
  p.dur = .1
  p.amp = .01*(i+5)

print ("simulate all")
pr()

try:
  a[1].simulate(True)
except:
  print ("nrn.Section.simulate method not available (not merged from do-not simulate branch?)")
  quit()

print ("simulate some")
for i in [1,3]:
  a[i].simulate(False)
pr()

print ("simulate all")
for s in a:
  s.simulate(True)
pr()

print ("simulate last")
for s in a[:-1]:
  s.simulate(0)
pr()

print ("simulate all")
a[0].simulate(-1)
pr()
