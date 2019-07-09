#now only in HocTopLevelInterpreter
names = ['ref', 'cas', 'allsec', 'Section', 'setpointer']

from neuron import h
o = h
d = dir(o)
for i in names:
  assert(i in d)
  print((eval("o.%s" % i).__doc__))

o = h.IClamp()
d = dir(o)
for i in names:
  assert(i not in d)
assert('get_segment' in d)
print((o.get_segment.__doc__))

print("success")

s = [h.Section(name='s'+str(i)) for i in range(5)]
print(s)
for sec in h.allsec():
  print((h.cas()))
r = h.ref("hello")
print((r[0] == 'hello'))

