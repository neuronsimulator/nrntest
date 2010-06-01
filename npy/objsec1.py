from neuron import h

class Cell(object):
  def __init__(self):
    self.soma = h.Section(self, name = 'soma')
    self.axon = h.Section(self, name = 'axon')
    self.dend = []
    for i in range(3):
      self.dend.append(h.Section(self))
    s = self.soma
    s.L = 10
    s.diam = 10
    s.insert('hh')
    for d in self.dend:
      d.connect(self.soma(0))
      d.nseg = 3
      d.L = 100
      d.diam = 2
      d.insert('pas')
      d.g_pas = .0001
      d.e_pas = -65
    a = self.axon
    a.connect(self.soma(1)) 
    a.nseg = 11
    a.L = 1000
    a.diam = 1
    a.insert('hh')

  def __str__(self):
    return 'Cell'

c = Cell()
h.topology()

