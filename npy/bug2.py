import neuron
h = neuron.h
sec = h.Section()
print(sec) 
sec.nseg = 3 
sec.insert("hh") # nrn.hh does gives assertion error and exits
sec.L = 20
print((sec.name()))
for seg in sec :
  print(("  x = ", seg.x, "  v = ", seg.v, "  diam = ", seg.diam, "  cm = ", seg.cm))
  for mech in seg :
    print(("   ", mech.name()))
    if mech.name() == "hh" :
      print(("      gnabar = ", mech.gnabar))

h("insert extracellular")
sec(.5).vext[0] = -30
sec(.5).vext[1] = -20
print((sec(.5).vext[0], sec(.5).vext[1]))
nd=sec(.5)
print((nd.vext[0], nd.vext[1]))
print((nd.xraxial[0], nd.xraxial[1], nd.xc[0], nd.xc[1], nd.xg[0], nd.xg[1]))
print((nd.e_extracellular))
