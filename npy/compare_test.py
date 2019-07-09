from neuron import h

def do_test(test, val, correct_val):
    print(('%30s   %8r  %8r  %s' % (test, val, correct_val, 'passed' if val == correct_val else 'failed')))

a = h.ref(0)
b = h.ref(0)
c = h.ref('foo')
d = c
v = h.Vector([1, 2])
h('double x[3][2][2]')
h('double y[3][2]')
h('double z1[2], z2[2]')
h('''
proc xaxis() {
}
''')
g = h.Graph(0)
g2 = h.Graph(0)

print("""
                          Test      Value  Expected  Result
-----------------------------------------------------------""")

do_test('a==a', a==a, True)
do_test('a==b', a==b, False)
do_test('a!=b', a!=b, True)
do_test('d==c', d==c, True)
do_test('h._ref_t == h._ref_t', h._ref_t == h._ref_t, True)
do_test('h._ref_t < h._ref_t', h._ref_t < h._ref_t, False)
do_test('h._ref_t == v._ref_x[0]', h._ref_t == v._ref_x[0], False)
do_test('h._ref_z1 == h._ref_z1', h._ref_z1 == h._ref_z1, True)
do_test('h._ref_z1 == h._ref_z2', h._ref_z1 == h._ref_z2, False)
do_test('h.Vector().x == h.Vector().x', h.Vector().x == h.Vector().x, False)
do_test('h.Vector(5).x == h.Vector(3).x', h.Vector(5).x == h.Vector(3).x, False)
do_test('h.x[1] == h.x[1][0]', h.x[1] == h.x[1][0], False)
do_test('h.x[1] == h.y[1]', h.x[1] == h.y[1], False)
do_test('h.xpanel == h.xpanel', h.xpanel == h.xpanel, True)
do_test('h.xpanel == h.xvalue', h.xpanel == h.xvalue, False)
do_test('h.xaxis == g.xaxis', h.xaxis == g.xaxis, False)
do_test('g.xaxis == g.xaxis', g.xaxis == g.xaxis, True)
do_test('g.xaxis == g2.xaxis', g.xaxis == g2.xaxis, False)
do_test('g != g2', g != g2, True)
