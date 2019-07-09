from neuron import h

def u(n):
  print(n, h.units(n))

u('t')
u('dt')
u('celsius')
u('v')
u('Ra')
u('gnabar_hh')
u('ina')
u('nao')
u('nai')
u('ena')
u('ExpSyn.g')
u('ExpSyn.i')
u('ExpSyn.e')

h('a=1')
h.units('a', 'inch')
u('a')

