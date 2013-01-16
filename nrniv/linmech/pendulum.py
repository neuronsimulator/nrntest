from neuron import h
from math import cos, sin, fabs

h.load_file('nrngui.hoc')

cmat = h.Matrix(2,2,2).ident()

gmat = h.Matrix(2,2,2)
gmat.setval(0,1, -1)
gmat.setval(1,0,  1) # not needed unless experimenting with z2 below

y = h.Vector(2)
y0 = h.Vector(2)
b = h.Vector(2)

def callback():
  #print 'callback t=', h.t
  z1 = y.x[0]
  z2 = -fabs(cos(z1)) # jacobian element is db[1]/dy[0]
  z2 = 0
  gmat.setval(1,0, z2)
  b.x[1] = -sin(z1) + z1*z2

nlm = h.LinearMechanism(callback, cmat, gmat, y, y0, b)


dummy = h.Section()
trajec = h.Vector()
tvec = h.Vector()
trajec.record(y._ref_x[0])
tvec.record(h._ref_t)

graph = h.Graph()
h.tstop=50

def prun(theta0, omega0):
  graph.erase()
  y0.x[0] = theta0
  y0.x[1] = omega0
  h.run()
  trajec.line(graph, tvec)

h.dt /= 10
h.cvode.atol(1e-5)
h.cvode_active(1)
prun(0, 1.9999) # 2.0001 will keep it rotating
graph.exec_menu("View = plot")

