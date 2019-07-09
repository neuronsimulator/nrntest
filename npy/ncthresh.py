from neuron import h
soma = h.Section()
nc = h.NetCon(soma(.5)._ref_v, None)
nc.threshold = -20

tvec = h.Vector()
def p() :
  print(h.t, soma(.5).v)

nc.record(p)
nc.record(tvec)

h.finitialize(-60)
while h.t < 100 :
  soma(.5).v = h.t - 50.
  h.fadvance()

tvec.printf()

