#pc.py_alltoall(dict) is an error
from neuron import h
pc = h.ParallelContext()
nhost = int(pc.nhost())
rank = int(pc.id())
err = 1

# A nice improvement to pc.py_alltoall() is that it accept a dict as an arg.
if pc.nhost() > 1:
  if pc.id() == 0:
    print((0))
  pc.barrier()
  quit()

src = {i:(100+i) for i in range(nhost)}
#print(src)

try:
  dest = pc.py_alltoall(src)
  err = 1
except:
  err = 0

err = int(pc.allreduce(err, 1))
print(err)
h.quit()

