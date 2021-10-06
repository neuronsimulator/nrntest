from neuron import h
from time import sleep

pc = h.ParallelContext()


def f(arg):
    sleep(0.1)
    x = arg * arg
    print("%d %g = f(%g)" % (pc.id(), x, arg))
    return x


pc.runworker()

for i in range(5):
    pc.submit(f, i)
i = 5

x = 0
while pc.working():
    r = pc.pyret()
    x += r
    print("f(%g)=%g  x=%g" % (pc.upkscalar(), r, x))
    if i < 10:
        pc.submit(f, i)
        i += 1

pc.done()
h.quit()
