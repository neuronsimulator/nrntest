from neuron import h

pc = h.ParallelContext()
nhost = int(pc.nhost())
rank = int(pc.id())


def _chk(a, b):
    import pickle

    s1 = str(a)
    s2 = str(b)
    if "Vector" in s1:
        s1 = pickle.dumps(a)
        s2 = pickle.dumps(b)
    if s1 != s2 or False:
        print(s1)
        print(s2)
    assert s1 == s2


def chkallgather(x):
    y = [x] * nhost
    _chk(pc.py_allgather(x), pc.py_alltoall(y))


def chkgather(x, root):
    y = [None] * nhost
    y[root] = x
    y = pc.py_alltoall(y)
    y = y if rank == root else None
    _chk(pc.py_gather(x, root), y)


def chkbroadcast(x, root):
    y = [x] * nhost if rank == root else [None] * nhost
    y = pc.py_alltoall(y)[root]
    _chk(pc.py_broadcast(x, root), y)
    x = x if rank == root else None
    _chk(pc.py_broadcast(x, root), y)


def chkscatter(xl, root):
    y = xl if rank == root else [None] * nhost
    y = pc.py_alltoall(y)[root]  # value comes from root rank
    _chk(pc.py_scatter(xl, root), y)  # irrelevant data for nonroot ranks
    xl = xl if rank == root else None
    _chk(pc.py_scatter(xl, root), y)  # None for nonroot ranks


def chkscatteralt(x, root):
    xl = [x if i % 2 == 0 else None for i in range(nhost)]
    chkscatter(xl, root)


def chk(x):
    chkallgather(x)
    chkgather(x, 0)
    chkgather(x, nhost - 1)
    chkbroadcast(x, 0)
    chkbroadcast(x, nhost - 1)
    chkscatteralt(x, 0)
    chkscatteralt(x, nhost - 1)


def test():
    chk(None)
    chk("hello")
    chk(True)
    chk(float(rank))
    chk(rank)
    chk(h.Vector(1).fill(rank))
    chk({str(rank): rank})
    chk([])
    chk([rank, 2 * rank])


import sys

nonecount = sys.getrefcount(None)

test()


def bigtest(n):
    for i in range(2):
        test()
    for j in range(n):
        pc.barrier()
        if rank == 0:
            print(("checkleak %d of up to %d" % (j, n)))
        sz = h.nrn_mallinfo(1)
        for i in range(1000):
            test()
        sz = h.nrn_mallinfo(1) - sz
        print(("%d sizedif = %d" % (rank, sz)))
        sz = pc.allreduce(sz, 1)
        if sz == 0 and j > 0:
            break


# bigtest(10)

# print("%d change in nonecount %d from %d" % (rank, sys.getrefcount(None) - nonecount, nonecount))

pc.barrier()
if rank == 0:
    print((0))
h.quit()
