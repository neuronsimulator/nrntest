import hoc
h = hoc.HocObject()

h('''
create axon, soma, dend[3]
connect axon(0), soma(0)
for i=0, 2 connect dend[i](0), soma(1)
axon { nseg = 5  L=100 diam = 1 insert hh }
forsec "dend" { nseg = 3 L=50 diam = 2 insert pas e_pas = -65 }
soma { L=10 diam=10 insert hh }
''')

print(h.axon.name())
print(h.dend)
print(h.dend[1])
print(h.dend[1].name())

import sys
def e(stmt) :
  try:
    print(stmt)
    exec(stmt)
  except:
    print(sys.exc_info()[0], ': ', sys.exc_info()[1])

e('h.axon = 1')
e('h.dend[1] = 1')


from nrn import * # otherwise hh needs to be nrn.hh
print(h)
print(h.axon)
print(h.axon.name())
print(h.axon(.5))
print(h.axon(.5).hh)
print(h.axon(.5).hh.name())
print(h.axon(.5).hh.gnabar)
