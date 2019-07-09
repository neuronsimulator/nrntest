import neuron
h = neuron.h

h('proc chx() { $&1 = 2 }')

x = 10
print(x) # 10
y = h.ref(x)
print(y[0]) # 10.0
h.chx(y)
print(y[0], x) # 2.0 10
x=20
print(y[0], x) # 2.0 20

from e import *
e('h._ref_x')
e('h._ref_sin')
h('x=5')
y = h._ref_x
print(y)
print(h.x, y[0])
h.x = 6
print(h.x, y[0])
y[0] = 7
print(h.x, y[0])

h('''
begintemplate A
public x
proc init() { x = 1 }
endtemplate A
''')

class B(neuron.hclass(h.A)) :
  x = 0 # overrides h.A.x
  def __init__(self) :
    self.x = 2

b = B()
print(b.x, b.baseattr('x'))

y=b._ref_x
print(y)
y[0] = 3
print(y[0], b.x, b.baseattr('x'))

v = h.Vector(5).indgen()
y = v._ref_x[0]
print(y)
y[2] = 20
v.printf()
y = v._ref_x[1]
y[2] = 30
v.printf()
print(v.x[2], y[2])
