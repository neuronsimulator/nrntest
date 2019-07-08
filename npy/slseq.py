from neuron import h
a = [h.Section(name='s%d'%i) for i in range(3)]
sl = h.SectionList()
for s in a:
  sl.append(sec=s)

for s in sl:
  print(s)
print("")

for x in sl:
  for y in sl:
    print (x, y)
print("")

h('''
objref z
z = new PythonObject()
z = z.sl
''')
for x in h.z:
  for y in h.z:
    print (x, y)

h('objref z')
sl = h.Vector()
sls = h.List("SectionList")
print ("number of SectionList", sls.count())
h.allobjects()
