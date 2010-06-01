import neuron
h = neuron.h
postCell = h.Section()
postCell.L = 20
postCell(0.5).diam = 20
#myMech = h.ExpSyn(0.5, sec = postCell)
myMech = h.ExpSyn(postCell(0.5))

preCell0 = h.Section()
preCell0.L = 20
preCell0(0.5).diam = 20
preCell0.insert('pas')
preCell0.insert('hh')
h.NetCon(preCell0(0.5)._ref_v, myMech, sec = preCell0)
