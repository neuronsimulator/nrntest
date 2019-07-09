import neuron
h = neuron.h

h('''
load_file("nrngui.hoc")
create soma
L = 10
diam = 100/(L*PI)
insert hh
stdinit()
''')

sec = h.cas()
print(sec.name())

for m in sec(.5) :
 print(m , m.name())

print(sec(.5).hh.gnabar)

sec.insert('pas')
for m in sec(.5) :
 print(m , m.name())

