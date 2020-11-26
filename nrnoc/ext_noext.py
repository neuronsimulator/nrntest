# extracellular: if ax[0] has extracellular and ax[1] does not, how
# are they coupled? ie. is ax[0](1).vext[0] always 0 (grounded)?

from neuron import h, gui

class Cell():
  def __init__(self, id, node_extracell=0):

    nnode = 3
    self.nnode = nnode
    self.id = id

    self.nodes = [h.Section(name='node%d'%i, cell=self) for i in range(nnode)]
    self.internodes = [h.Section(name='internode%d'%i, cell=self) for i in range(nnode-1)]

    for i in self.nodes:
      i.L = 1
      i.diam = 1
      i.nseg = 1
      i.insert('hh')
      if node_extracell:
        i.insert("extracellular")
        for seg in i:
          seg.xraxial[0] = 1e-6

    for i in self.internodes:
      i.L = 100
      i.diam = 0.5
      i.nseg = 5
      i.insert('hh')
      i.insert('extracellular')
      for seg in i:
        seg.xg[0] = .00001
        seg.xc[0] = .01
        seg.xraxial[0] = 1e3

    for i, internode in enumerate(self.internodes):
      internode.connect(self.nodes[i](1))
      self.nodes[i+1].connect(self.internodes[i](1))

    ic = h.IClamp(self.nodes[0](.5))
    self.ic = ic
    ic.delay = 0.1
    ic.dur = 0.1
    ic.amp = 0.4

  def __str__(self):
    return "Cell" + str(self.id)

cells = [Cell(i, node_extracell=i) for i in [0,1]]
h.load_file("nodemy.ses")

def move_ic(end):
  for i in cells:
    ix = -1 if end == 1 else 0
    i.ic.loc(i.nodes[ix](.5))
