from neuron import h

def test():
  sections=[h.Section() for _ in range(10)]
  for sec in sections:
    nseg=11
    sec.insert('hh')
    sec.insert('pas')

  i=0
  for sec in h.allsec():
    for sec2 in h.allsec():
      for seg in sec:
        for seg2 in sec2:
          for mech in seg:
            for mech2 in seg2:
              i += 1

  j=0
  for sec in iter(h.allsec()):
    for sec2 in iter(h.allsec()):
      for seg in iter(sec):
        for seg2 in iter(sec2):
          for mech in iter(seg):
            for mech2 in iter(seg2):
              j += 1

  assert(j == i)
  return i

def testsz(n):
  sz = h.nrn_mallinfo(1)
  for i in range(n):
    k = test()
    sz1 = h.nrn_mallinfo(1) - sz
    print("%d %d size=%d" % (i, k, sz1))

if '__main__' == __name__:
  testsz(50)
