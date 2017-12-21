
from neuron import h
pc = h.ParallelContext()

import time
pc.subworlds(2)
nhost_world = int(pc.nhost_world())
id_world = int(pc.id_world())
nhost_bbs = int(pc.nhost_bbs())
id_bbs = int(pc.id_bbs())
nhost = int(pc.nhost())
id = int(pc.id())
def f(arg):
  print ("arg=%d world (%d of %d)  bbs (%d of %d)  id/nhost (%d of %d)"%
    (arg, id_world, nhost_world, id_bbs, nhost_bbs, id, nhost))

f(1)
time.sleep(.1) #enough time to print

pc.runworker()
print ("after runworker")
pc.context(f, 2)
f(3) #rank 0 of the master subworld

for i in range(5): #time to print and
  pc.post("wait")   # bulletin board to communicate
  time.sleep(.1)
  pc.take("wait")

pc.done()
h.quit()
