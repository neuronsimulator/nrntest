from neuron import h

h('''

x=5
double y[4]

func f() { return 6 }

begintemplate A
proc call() {
  $o1._()
}
endtemplate A
''')

def callback():
  print('callback')
  print(h.f())
  h.x = 4
  print(h.x)
  h.y[2] = 6
  print(h.y[2])


a = h.A()
a.call(callback)

from neuron import h, nonvint_block_supervisor
h.load_file('stdrun.hoc')

_callbacks = [None]*11
_callbacks[1] = callback
nonvint_block_supervisor.register(_callbacks)

#h.cvode_active(0)
h('''
begintemplate B
proc call() {
  // anything that ends up calling a nonvint_block_supervisor callback
  // that calls 'def callback' within this context
  finitialize()
}

endtemplate B
''')

h.finitialize()
print('ok so far')
b = h.B()
b.call()
