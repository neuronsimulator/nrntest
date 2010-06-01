from nrn import *

cable = Section()
cable.nseg = 5
cable.L = 1000
cable.insert('hh')

print cable.name(), cable(.5).hh.gnabar

print "for seg in cable.allseg()"
for seg in cable.allseg() :
  print seg, seg.x
  x = seg.x
  if x > 0 and x < 1 :
    print x, seg.hh.gnabar, seg.v

print "for seg in cable"
for seg in cable : # only the internal compartments
  x = seg.x
  print x, seg.hh.gnabar, seg.v


cable.nseg = 2
print 'triple loop over 2 segs of cable'
for s1 in cable :
  for s2 in cable :
    for s3 in cable :
      print s1.x, s2.x, s3.x

print 'alternating triple loop of cable'
for s1 in cable.allseg() :
  for s2 in cable :
    for s3 in cable.allseg() :
      print s1.x, s2.x, s3.x

print 'alternating triple loop of cable'
for s1 in cable :
  for s2 in cable.allseg() :
    for s3 in cable :
      print s1.x, s2.x, s3.x

