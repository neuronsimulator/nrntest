from neuron import *

h('''
begintemplate A
public x, s, o, xa, oa, f, p
strdef s
objref o, oa[2]
double xa[3]
proc init() { \
  x = $1 \
}
func f() { return $1*xa[$2] }
proc p() { x += 1 }
endtemplate A
''')

class A1(hclass(h.A)) :
  def __init__(self, arg) : # note, arg used by h.A
    #self.bp = hoc.HocObject.baseattr(self, 'p')
    self.bp = self.baseattr('p')
  def p(self) :
    self.bp()
    return self.x

a = A1(5)

print a.x == 5.0
print a.p() == 6.0

b = A1(4)
a.s = 'one'
b.s = 'two'
print a.s == 'one'
print b.s == 'two'
print h.A[0].s == 'one'
print a.p() == 7.0
print b.p() == 5.0
a.a = 2
b.a = 3
print a.a == 2
print b.a == 3

print h.List('A').count() == 2
a=1
b=1
print h.List('A').count() == 0

