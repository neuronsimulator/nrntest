from neuron import h
h('''
begintemplate HCell
public soma
create soma
endtemplate HCell
''')

class PCell(object):
  def __init__(self):
    self.soma = h.Section(name='soma', cell=self)

s1 = h.Section(name='soma')
h('create soma')
c1 = PCell()
c2 = h.HCell()

for sec in h.allsec():
  print sec.name(), sec.cell()

print c2.hname(), c2.soma.cell().hname()
