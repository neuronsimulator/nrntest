from neuron import h

s = h.Section(name="soma")
s.insert('hh')
for sec in h.allsec():
  #sname="h." + h.secname(sec=sec)
  sname="h." + sec.hoc_internal_name()
  for seg in sec:
    for mech in seg:
      mechname = mech.name()
      ision = mech.is_ion()
      for n in dir(mech):
        if "__" not in n and n not in ['name', 'next', 'is_ion', 'segment']:
          nm = "%s(%g).%s.%s"%(sname, seg.x, mech.name(), n)
          print ("%s = %s" % (nm, str(eval(nm))))
          if ision:
            nm = "%s(%g).%s"%(sname, seg.x, n)
          else:
            nm = "%s(%g).%s_%s"%(sname, seg.x, n, mechname)
          print ("%s = %s" % (nm, str(eval(nm))))

