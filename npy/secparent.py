from neuron import h

# many combinations of orientation and connection position of parent/child

def remake(n, hocworld=False):
  global root, parent, child
  h.execute1('forall delete_section()', 0)
  parent = None
  if hocworld:
    h('create root, child')
    root = h.root
    child = h.child
    if n > 0:
      h('create parent[%d]'%n)
      parent = [h.parent[i] for i in range(n)]
  else:
    root = h.Section(name='root')
    child = h.Section(name='child')
    if n > 0:
      parent = [ h.Section(name='parent[%d]'%i) for i in range(n)]
  for sec in h.allsec():
    sec.nseg = 3

def name(sec, x):
  s1 = '%s(%g)'%(sec.name(), x)
  return s1

def info(sec, pr=False):
  o = sec.orientation()
  s1 = name(sec, o)
  p = sec.parentseg()
  s2 = name(p.sec, p.x) if p else "None"
  tp = sec.trueparentseg()
  s3 = name(tp.sec, tp.x) if tp else "None"
  if pr:
    h.topology()
    print '%s parent: %s trueparent: %s'%(s1, s2, s3)
  return (o, p.x, s3)

for rx in [0,.1,1]:
  s3 = 'root(%g)'%rx if rx != 0 else 'None'
  for o in [0,1]:
    for z in [False, True]:
      remake(0, z)
      child.connect(root(rx), o)
      r = info(child)
      if r != (o,rx,s3):
        print r, (o, rx,s3)
        assert(r == (o, rx, s3))

np = 2
def allbits(np):
  r = [0]*np
  for i in range(2**np):
    for j in range(np):
      r[j] = (i/(2**j))%2
    yield r


for rx in [0, .1, 1]:
  for co in [0,1]:
    for z in [False]:
      for po in allbits(2):
        for pa in allbits(2):
          if pa[0] == 0:
            continue
          remake(np, z)
          child.connect(parent[np-1](pa[np-1]), co)
          for i in range(1,np):
            parent[i].connect(parent[i-1](pa[i]), po[i])
          parent[0].connect(root(rx), po[0])
          r = info(child, True)
          '''
          manually inspect for correctness
          if r != (co, pa[np-1], s3):
             print r, (co, pa[np-1], s3)
             assert(r ==(co, pa[np-1], s3))
          '''

remake(4, False)
print root.children()
for i in range(4):
  parent[i].connect(root(i/4.))
c = root.children()
print c
for s in c:
  print s.parentseg().x

