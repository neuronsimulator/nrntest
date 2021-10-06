from neuron import h
from time import sleep

pc = h.ParallelContext()


def f(i, hvec):
    sleep(0.1)
    hvec.reverse()
    pc.post(i, pc.id(), hvec)
    return hvec.sum()


pc.runworker()

for i in range(5):
    pc.submit(f, i, h.Vector(4).indgen().add(i * 100))

x = 0
while pc.working():
    i = int(pc.upkscalar())  # the first arg of f
    va = pc.upkvec()  # the second arg of f
    x += pc.retval()
    pc.take(i)
    pid = int(pc.upkscalar())
    v = pc.upkvec()
    print(("i=", i, "from host", pid, list(va), list(v)))

pc.done()
h.quit()
