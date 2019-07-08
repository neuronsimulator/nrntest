from e import e
from neuron import h

h('''
begintemplate Foo
public foo, _ref_foo
proc init() {
  foo = 1
  _ref_foo = 2
}
endtemplate Foo
''')

s = h.Section()

f = h.Foo()
e('h.setpointer(s(.5)._ref_v, "foo", f)')
e('f._ref_foo = s(.5)._ref_v')
e('f.foo = s(.5)._ref_v')

