import neuron
h = neuron.h
import sys
def e(stmt) :
  try:
    print stmt
    exec(stmt)
  except:
    print sys.exc_info()[0], ': ', sys.exc_info()[1]

h(''' create soma
insert hh
''')

e('print sec(.5).vext[5]')
sec = h.cas()
e('print sec(.5).vext[1]')
e('print sec(.5).vext[5]')
h('insert extracellular')
e('print sec(.5).vext[5]')
e('print sec(.5).gnabar_hh[0]')
e('print sec(.5).foo')
e('print sec(2).gnabar_hh')
e('print sec(-1).gnabar_hh')
e('print sec(.5).pas.g')
e('print sec(.5).g_pas')
