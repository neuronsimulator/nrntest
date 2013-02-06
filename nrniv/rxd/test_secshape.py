from neuron import h
from neuron import section_shape_supervisor as sss
import numpy

s = h.Section(name='soma')
s.L = 10
s.diam = 5

def area_ri(sec):
  print 'area_ri ', sec.name()
  a = numpy.zeros(3*sec.nseg)
  for i, seg in enumerate(sec):
    r_pside = .1
    r_cside = .2
    area = 100.
    a[3*i] = r_pside
    a[3*i+1] = area
    a[3*i+2] = r_cside
  return a

def pr(sec):
  for seg in sec.allseg():
    print sec.name(), seg.x, h.area(seg.x, sec=sec), h.ri(seg.x, sec=sec)
pr(s)

sss.register(s, area_ri, None)
h.finitialize()
pr(s)
