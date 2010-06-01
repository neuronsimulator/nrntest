import hoc
h = hoc.HocObject()

h('''
begintemplate Cell
public axon, soma, dend
create axon, soma, dend[3]
proc init() { local i \
  connect axon(0), soma(0) \
  for i=0, 2 connect dend[i](0), soma(1) \
  axon { nseg = 5  L=100 diam = 1 insert hh } \
  forsec "dend" { nseg = 3 L=50 diam = 2 insert pas e_pas = -65 } \
  soma { L=10 diam=10 insert hh } \
}
endtemplate Cell
obfunc newcell() { return new Cell() }
''')

c = h.newcell()
print c.axon.name()
print c.dend
print c.dend[1]
print c.dend[1].name()

import sys
def e(stmt) :
  try:
    print stmt
    exec(stmt)
  except:
    print sys.exc_info()[0], ': ', sys.exc_info()[1]

e('c.axon = 1')
e('c.dend[1] = 1')


from nrn import * # otherwise hh needs to be nrn.hh
print c
print c.axon
print c.axon.name()
print c.axon(.5)
print c.axon(.5).hh
print c.axon(.5).hh.name()
print c.axon(.5).hh.gnabar

print c.dend[1].name()
print c.dend[1](.5)
print c.dend[1](.5).pas
print c.dend[1](.5).pas.name()
print c.dend[1](.5).pas.g

