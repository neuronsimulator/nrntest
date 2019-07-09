from e import e
from neuron import h
h('''
a = 10
double d[2][2]
d[0][0] = 100
d[1][1] = 101

func f() {return 0}
begintemplate A
public a, f, d
double d[2][2]
proc init() { a = 5 d[0] = 50 d[1] = 51}
func f() { return 1 }
endtemplate A
objref b[3]
b[0] = new A()
''')

e('print (h.a)')
e('print (h.b.a)')
e('print (h.b[0].a)')
e('print (h.b.f())')
e('print (h.b[0].f())')
e('print (h.b.b.b.b.a)')
e('print (h.f.a)')
e('print (h.b[0].f.a)')
e('print (h.d.a)')
e('print (h.d[0].a)')
e('print (h.d[0][0].a)')
e('print (h.b[0].d.a)')
e('print (h.b[0].d[0].a)')

e('h.b.__dict__')
e('h.b.__doc__')
e('h.b[0].d.__dict__')
e('h.b[0].d.__doc__')

