#mpiexec --oversubscribe -n 8 nrniv -python -mpi alltoallleak.py
import os
from neuron import h
pc = h.ParallelContext()
import sys
tmp = {i:list(range(1000)) for i in range(1000)}
data = [tmp for i in range(int(pc.nhost()))]


a = 0
for i in range(10000):  
    foo = pc.py_alltoall(data)
    if pc.id()==0:
        if i%150==0:
          if False:
            tot_m, used_m, free_m = list(map(int, os.popen('free -t -m').readlines()[-1].split()[1:]))
            print(('mem used ' + str(used_m/1000.0)))
            sys.stdout.flush()
          elif False:
            print(h.nrn_mallinfo(1))
            sys.stdout.flush() # prevent increase due to print when stdout is file
          else:
            # reduce print size and make it more likely to compare with
            #other versions
            b = h.nrn_mallinfo(1)
            #print("(%d %d %d)"%(i, b, b-a))
            #sys.stdout.flush()
            if a != b:
              print("%d %d"%(i, b-a))
              sys.stdout.flush()
            a = b

pc.barrier()
h.quit()
