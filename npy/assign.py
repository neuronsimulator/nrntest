import neuron
h = neuron.h
h('''x=1
double y[3]
strdef s
objref o, oo[5], o1, o2, o3, o4
''')

h.x = 2
h.y[1] = 10
h.s = "hello"
h.o = {}
h.oo[0] = []
h.oo[1] = h.List()
h.oo[2] = 25
h.oo[3] = 'goodbye'
h.oo[4] = None
print((h.x, h.y[1], h.s, h.o, h.oo[0], h.oo[1], h.oo[2], h.oo[3], h.oo[4]))

h.o1 = 25
h.o2 = 'another'
h.o3 = h.Vector()
h.o4 = None
h('printf("%s %s %s %s %s\\n", o, o1, o2, o3, o4)')
print((h.o, h.o1, h.o2, h.o3, h.o4))

h=0

