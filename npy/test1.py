import hoc
hoc.execute('print "scalar get tests"')
h = hoc.HocObject()
print(h)
h('print "goodbye"')
h('x = 2')
print(h.x)

h('strdef str')
h('str = "test hoc string"')
print(h.str)

h('objref obj')
h('obj = new Vector(10)')
a = h.obj
print(a)

h('print "scalar set tests"')
h.x = 5
print(h.x)

h.str = 'from python'
print(h.str)

h('objref o2')
h('o2 = new List()')
h.obj = h.o2
print(h.obj)

h('print "function tests"')
f = h.printf
print(f)

h('func f() { print $1, $2, $3  return $1 }')
print(h.f(4.,5.,6.))
print(h.f(4,5,6))

print(h.sin(h.PI/2))
print(h.atan2(1, 2))

h('print "object component tests"')
h('objref vec')
h('vec = new Vector(5)')
h.vec.indgen().mul(10)
h.vec.printf()

h('objref ptr')
h('ptr = new Pointer(&x)')
print(h.ptr.val)
h.ptr.val = 6
h('print ptr.val')

h('print "array tests"')
print(h.vec.x[3])
h.vec.x[3] = 25
h('print vec.x[3]')

h('''
objref m
m = new Matrix(3,5)
for i=0, m.nrow-1 for j=0, m.ncol-1 m.x[i][j] = i*10 + j
''')
h.m.printf()
print(h.m.x[2][3])
h.m.x[2][3] = 123
h.m.printf()

h('''
double xx[3][4]
for i=0, 2 for j=0, 3 xx[i][j] = i*10 + j
''')
print(h.xx[2][1])
h.xx[2][1] = 121
h('print xx[2][1]')

print('more function tests')
h('obfunc newvec() { return new Vector($1) }')
h('obfunc newlist() { return new List() }')
vlist = h.newlist()
vlist.append(h.newvec(10).indgen().add(100))
vlist.append(h.newvec(11).indgen().add(200))
vlist.append(h.newvec(12).indgen().add(300))
print(vlist)
print(vlist.count())
print(vlist.object(1).x[10])

h('create soma')
h('print secname()')
print(h.secname())
vlist.object(0).label('python label')
print(vlist.object(0).label())

h('proc p() { print "inside p" }')
print(h.p())

h('objref stim')
h('stim = new IClamp(.5)')
h.stim.dur = 2
print('stim.dur = ', h.stim.dur)
h('print stim.dur')

print('common errors')
import sys
def e(stmt) :
  try:
    print(stmt)
    exec(stmt)
  except:
    print(sys.exc_info()[0], ': ', sys.exc_info()[1])

e('print h.foo')
e('h.foo = 5')
e('print h.vec.foo')
e('h.vec = 5')
e('h.vec.x = 5')
e('print h.vec[1]')
e('h.vec[1] = 5')
e('print h.vec.x[1][2]')
e('h.vec = h.m.x')
e('h.vec = h.m.x[1]')
e('h.m = 5')
e('h.m[1] = 5')
e('h.m.x = 5')
e('h.m.x = "error"')
e('h.m.x = h.vec')
e('h.m.x[1] = 5')
e('h.m.x[1][1][1] = 5')
e('h.xx[1] = 4')
e('h.xx[1][1][1] = 4')
e('print h.xx[1][1][1]')
e('h.xx = 4')
e('h.f = 1')
e('h.f(1,2,3) = 1')

h('''
begintemplate A
public size, x, xa, str, o, oa
double xa[1]
objref o, oa[1]
strdef str
proc init() { \
  size = $1 \
  double xa[$1] \
  objref oa[$1] \
  x = 1 \
  str = "begin" \
}
proc pr() { local i \
  printf("x=%g str=%s o=%s\\n", x, str, o) \
  for i=0, size-1 { printf(" %g", xa[i]) } printf("\\n") \
  for i=0, size-1 { printf(" %s", oa[i]) } printf("\\n") \
}
endtemplate A
obfunc newA() { return new A($1) }
''')

a = h.newA(3)
a.pr()

a.x = 2
a.str = 'reset'
a.o = h.newvec(2)
for i in range(0,int(a.size)) :
  a.xa[i] = 10 + i
  a.oa[i] = h.newvec(i)
a.pr()
print(a.x, a.str, a.o, a.xa[0], a.oa[0])

print("more errors")
e('a.x = a.str')
e('a.x = a.xa')
e('a.x = a.o')
e('a.x = a.oa')
e('a.x = a.oa[1]')
print(a.x)
e('a.str = a.x')
e('a.str = a.o')
e('a.str = a.xa[1]')
e('a.str = a.oa')
e('a.str = a.oa[1]')
print(a.str)
e('a.o = a.x')
e('a.o = a.str')
e('a.o = a.xa[1]')
e('a.o = a.oa')
e('a.oa[1] = h.m.x')
print(a.o)

h('objref oa[3]')
print(h.oa[1])

e('h.sin(1,2)')
e('h.sin()')
e('h.printf("%d\\n", h.str)')

