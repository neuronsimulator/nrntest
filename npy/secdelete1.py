#test of section destruction
from neuron import h
s = h.Section()
h.topology()
s = None
h.topology()

s = h.Section()
a = h.Section()
a.connect(s)
h.topology()
s = None
h.topology()
a = None
h.topology()

class Cell(object):
  def __init__(self):
    self.s = h.Section(self, name='soma')
    self.a = h.Section(self, name='axon')
    self.a.connect(self.s)

c = Cell()
h.topology()
c = None
h.topology()
