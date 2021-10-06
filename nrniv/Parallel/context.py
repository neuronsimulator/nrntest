from neuron import h
from time import sleep
pc = h.ParallelContext()

def f(arg):
  print(('%d f(%s)'%(pc.id(), arg)))
  pc.post('goodbye', (int(pc.id()), 'goodbye'))

pc.runworker()

pc.context(f, ('hello', 1))
for i in range(1, int(pc.nhost())):
  pc.take('goodbye')
  print((pc.upkpyobj()))

pc.done()
h.quit()
