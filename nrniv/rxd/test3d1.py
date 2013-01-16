
from neuron import h
from mayavi import mlab
from neuron.rxd import geometry3d

[s1, s2, s3] = [h.Section() for i in xrange(3)]

for s in h.allsec():
    s.diam = 1
    s.L = 5


s2.connect(s1)
s3.connect(s1)

tri_mesh = geometry3d.surface(h.allsec())
mlab.triangular_mesh(tri_mesh.x, tri_mesh.y, tri_mesh.z, tri_mesh.faces, color=(1, 0, 0))
mlab.show()

