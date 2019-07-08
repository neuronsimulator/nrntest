from neuron import h
sl = h.SectionList()
secs = [h.Section(name='s'+str(i)) for i in range(4)]

for sec in secs:
  sl.append(sec)

#all sections present
for i, sec in enumerate(sl):
  assert (sec == secs[i])

#invalid section does not appear in SectionList iteration
secs.remove(secs[1])
for i, sec in enumerate(sl):
  assert(sec == secs[i])

#can remove from SectionList
sl.remove(secs[0])
assert(sl.contains(secs[0]) == False)
for sec in secs[1:]:
  assert(sl.contains(sec) == True)

sl.printnames()
