#mpiexec -n 8 nrniv -python -mpi alltoallleak.py
import os
from neuron import h
pc = h.ParallelContext()
import sys
tmp = {i:range(1000) for i in range(1000)}
data = [tmp for i in range(int(pc.nhost()))]


for i in range(10000):  
    foo = pc.py_alltoall(data)
    if pc.id()==0:
        if i%150==0:
          if False:
            tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
            print('mem used ' + str(used_m/1000.0))
            sys.stdout.flush()
          else:
            print(h.nrn_mallinfo(1))

pc.barrier()
h.quit()
