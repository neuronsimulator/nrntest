# launch with neurondemo -python cvevent.py

import hoc
h = hoc.HocObject()
h('demo(3)')

def callback() :
  print h.t
  h.cvode.event(h.t + .1, 'p.callback()')

h('''
objref p
p = new PythonObject()
obfunc newfih() { return new FInitializeHandler($1, $s2) }
''')

fih = h.newfih(0, 'p.callback()')

h.run()


