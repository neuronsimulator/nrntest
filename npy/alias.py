from neuron import h

h('''
x = 3
begintemplate Foo
proc init() {
}
endtemplate Foo
''')

f = h.Foo()
sf = h.StringFunctions()
sf.alias(f, "bar", h._ref_x)
def p():
  print h.x, f.bar, f._ref_bar[0]
p()
f.bar = 5
p()
f._ref_bar[0] = 7
p()
h.x=9
p()
