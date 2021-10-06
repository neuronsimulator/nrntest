from neuron import h
import math

pc = h.ParallelContext()


def f(arg):
    for i in range(1000000):
        x = math.sin(i * 0.0001 / math.pi)
    return x


pc.runworker()

tt = h.startsw()

for i in range(100):
    pc.submit(f, i)

x = 0
while pc.working():
    x = pc.retval()

print(h.startsw() - tt)

pc.done()
h.quit()
