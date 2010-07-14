from neuron import h
h.load_file('nrngui.hoc')

#top level
soma = h.Section(name='soma')
dend = h.Section()
dend.connect(soma(.5))

h.topology()

soma.push()
h.load_file('temp.ses')
h.pop_section()

#class with no hname
class Cell1:
  def __init__(self):
    self.soma = h.Section(name='soma', cell=self)
    self.dend = h.Section(cell=self)
    self.dend.connect(self.soma(.5))

c1 = Cell1()

#class with hname
class Cell2:
  index = 0
  def __init__(self):
    self.soma = h.Section(name = 'soma', cell=self)
    self.dend = h.Section(cell=self)
    self.dend.connect(self.soma(.5))
    self.name = 'Cell2_'+str(Cell2.index)
    Cell2.index += 1

  def __str__(self):
    return self.name

c2list = []
for i in range(3):
  c2list.append(Cell2())


h.topology()
