from e import e

# explore hoc_execerror while in hoc_object_component
# when ocjump to h.f(...) has intervening python activity.
# want to use valgrind to check for python memory leak due to the ocjump.

from neuron import h

h('''
begintemplate Foo
public soma, b, s, dend
create soma, dend[2]
strdef s
objref b
proc init() {
  insert extracellular
  a = 0 // not public
  b = new List() // b  not subscriptable
  s = "hello"
}
endtemplate Foo
''')

# NEURON: xg wrong number of array dimensions
h('''proc p1() { $o1.soma.xg[0][0] }''')
e('h.p1(h.Foo())')

# NEURON: L section property can't have argument
h('''proc p2() { $o1.soma.L(1) }''')
e('h.p2(h.Foo())')

# NEURON: xq suffix not a range variable or section property
h('''proc p3() { $o1.soma.xq }''')
e('h.p3(h.Foo())')

# NEURON: [...](...) syntax only allowed for array range variables: x
h('''proc p4() { $o1.x[0](.5) }''')
e('h.p4(h.Vector())')

class X():
  def __init__(self, arg):
    self.a = arg
  def f(self):
    return 3
  def g(self):
    1/0

# NEURON: Cannot assign to a PythonObject function call: f
h('''proc p5() { $o1.f() = 5 }''')
e('h.p5(X(5))')

# TypeError: 'int' object is not subscriptable
# NEURON: Python get item failed: PythonObject[0]
h('''proc p6() { $o1.a[0] }''')
e('h.p6(X(5))')

# AttributeError: 'X' object has no attribute 'z'
# NEURON: No attribute: z
h('''proc p7() { $o1.z }''')
e('h.p7(X(5))')

# ZeroDivisionError: division by zero
# NEURON: PyObject method call failed: g
h('''proc p8() { $o1.g() }''')
e('h.p8(X(5))')

e('h.Foo().a') # not an error even though a not public ?!

# a not a public member of Foo
# NEURON: Foo a
e('h.p6(h.Foo())')

# NEURON: z : object prefix is NULL
e('h.p7(None)')

# NEURON: b :not right number of subscripts
h('''proc p9() { $o1.b[0] }''')
e('h.p9(h.Foo())')

# string can't have function arguments or array indices
h('''proc p10() { $o1.s[0] }''')
e('h.p10(h.Foo())')

# NEURON: sec : bad connect syntax
h('''create s1, d1
proc p11() {
  $o2.sec connect $o1.sec[1](0), .5
}
''')
e('h.p11(h.SectionRef(h.s1), h.SectionRef(h.d1))')

# NEURON: sec :no subscript allowed
h('''proc p12() { $o2.sec[0] { print secname() }}''')
e('h.p12(h.SectionRef(h.s1), h.SectionRef(h.d1))')

# NEURON: Section was deleted
h('''proc p13() { $o1.sec {delete_section()}
  $o1.sec { print secname() }
}''')
e('h.p13(h.SectionRef(h.s1))')

# Foo[1].soma connection to Foo[1].soma will form a loop
# is this in component?
h('''proc p14() { $o2.soma connect $o2.soma(1), .5 }''')
e('h.p14(h.Foo(), h.Foo())')

#bad stack access: expecting (double); really (Object *)
h('''proc p14() { connect $o1.soma(1), $o2.soma }''')
e('h.p14(h.Foo(), h.Foo())')

#NEURON: subscript out of range dend
h('''proc p14() { $o2.soma connect $o1.dend[3](1), .5 }''')
e('h.p14(h.Foo(), h.Foo())')

#cannot figure out how to get bad connect syntax for case SECTION

#bad stack access: expecting (double); really (Object *)
h('''proc p14() { $o2.soma connect $o1, .5 }''')
e('h.p14(h.Foo(), h.Foo())')

#bad stack access: expecting (double); really (Object *)
h('''proc p15() {$o2.soma {connect $o1.dend[1](0), .5}}''')
# NEURON: soma :not right number of subscripts
e('h.p15(h.Foo(), h.Foo())')

