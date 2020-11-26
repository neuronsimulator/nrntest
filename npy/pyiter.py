from neuron import h

s = h.Section(name="soma")
s.nseg = 3
s.insert("pas")
s.insert("hh")

#print ("a")
a = []
for sec in h.allsec():
  for seg in sec:
    for m in seg:
      for var in m:
        a.append("%s(%g).%s.%s" % (sec.name(), seg.x, m.name(), var.name()))

#print ("b")
b = []
for sec in iter(h.allsec()):
  for seg in iter(sec):
    for m in iter(seg):
      for var in iter(m):
        b.append("%s(%g).%s.%s" % (sec.name(), seg.x, m.name(), var.name()))

if a == b:
  print (True)
else:
  print (a)
  print (b)

    
