from neuron import h

a = h.Section(name='bob')
b = h.Section(name='bob')
print (a.same(b), a is b, a == b) == (False, False, False)
c = h.cas()
print (c.same(a), c == a, c.same(b), c is a, c is b) == (True, True, False, True, False)
h('create s, d')

print (h.s.same(h.s), h.s is h.s, h.s == h.s) == (True, False, True)

print h.s.same(5) == False
print (h.s == 5) == False

h('objref vv')
h('vv = new Vector(3)')
print (h.vv == h.vv, h.vv.same(h.vv)) == (False, True)
