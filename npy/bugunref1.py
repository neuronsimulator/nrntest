from neuron import h

class foo(object):
  def bar(self):
    return h.Vector()


h('''
objref p0, p, y
p0 = new PythonObject()
p = p0.foo()
proc me() { localobj x \
  x = p.bar() \
  y = p.bar() \
  print x, y \
}
''')

vl = h.List('Vector')
print vl.count()
l = []
for i in range(5):
  h.me()
print vl.count()

