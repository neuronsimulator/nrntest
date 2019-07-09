import neuron
h = neuron.h
v = h.Vector()
v.resize(5).indgen().add(10)
v.printf()

h.printf('%s\n', None)
h('objref a')
print((h.a == None))

h('double d[3]')
for x in h.d :
  print(x)

for x in v :
  print(x)

h('''objref o[2][3], nil
for i=0,1 for j=0,2 { \
    o[i][j] = new List() \
    for k=0, 2 { \
      o[i][j].append(new Vector(3)) \
      o[i][j].object(k).indgen.add(i*1000 + j*100 + k*10) \
    } \
}
''')
for a in h.o :
  for b in a :
    for c in b :
      for d in c:
       print((a, b, c, d))

print((len(h.d)))
print((len(v)))
print((h.o, len(h.o)))
print((h.o[1], len(h.o[1])))
print((h.o[1][2], len(h.o[1][2])))
print((h.o[1][2][1], len(h.o[1][2][1])))
print((h.Vector[0], h.Vector[0][2]))
print(('number of hoc List instances ', len(h.List)))
for x in h.List :
  print(x)

h('o[1][1] = nil')
for x in h.List :
  print(x)

vt = h.Vector
v = vt(4)

h=0
v=0
x=0
a=0
b=0
c=0
d=0
vt=0

