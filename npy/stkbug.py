from neuron import h

class A(object):
  def __init__(self, arg):
    self.a = arg
    self.b = [arg, arg+1, arg+2]

h('objref po, p1')
h.po = A(3.14)

for i in range(10000):
  h.po.a = i
  if h.po.a != i:
    print i, h.po.a

h('for i=1,10000 po.a = i')
print h.po.a == 10000
h('for i=1,10000 po.b[2] = i')
print h.po.b[2] == 10000
