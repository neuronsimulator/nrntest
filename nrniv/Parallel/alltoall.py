from neuron import h

pc = h.ParallelContext()
nhost = int(pc.nhost())
rank = int(pc.id())

# Keep host output from being intermingled.
# Not always completely successful.
import sys


def serialize():
    for r in range(nhost):
        pc.barrier()
        if r == rank:
            yield r
    pc.barrier()


data = [(rank, i) for i in range(nhost)]

for r in serialize():
    if r == 0:
        f = open("temp", "w")
        f.write("source data\n")
        f.flush()
        f.close()
    f = open("temp", "a")
    f.write(str(rank) + str(data) + "\n")
    f.flush()

data = pc.py_alltoall(data)

for r in serialize():
    if r == 0:
        f = open("temp", "a")
        f.write("destination data\n")
        f.flush()
        f.close()
    f = open("temp", "a")
    f.write(str(rank) + str(data) + "\n")
    f.flush()

if rank == 0:
    from os import system

    print((system("cmp temp alltoall.cmp")))

pc.barrier()
h.quit()
