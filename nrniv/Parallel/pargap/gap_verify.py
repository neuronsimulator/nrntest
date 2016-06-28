from neuron import h

rank = int(h.pc.id())
nhost = int(h.pc.nhost())

sid2src = {}  # sid key specifies only one source (globally but only tested locally)
src2sids = {} # possibly several sids associated with same src
sid2tars = {} # possibly several targets associated with same sid
tar2sid = {}  # target key has only one sid

def target_var(g, id):
  sid = int(id)
  if tar2sid.has_key(g):
    print '%d %s with sid %d reregistered with sid %d'%(rank,g.hname(),tar2sid[g],id)
    raise RuntimeError
  tar2sid.update({g:sid})
  if sid2tars.has_key(sid):
    sid2tars[sid].append(g)
  else:
    sid2tars.update({sid:[g]})

def source_var(x, id):
  sid = int(id)
  sec = h.cas()
  seg = sec(x)
  if sid2src.has_key(sid):
    s1 = h.secname(sec = sid2src[sid].sec)
    s2 = h.secname(sec = sec)
    print '%d source var sid %d already in use for %s and %s'%(rank,id,s1,s2)
    raise RuntimeError
  sid2src.update({sid:seg})
  if src2sids.has_key(seg):
    src2sids[seg].append(sid)
  else:
    src2sids.update({seg:[sid]})

def rank2frac(r):
  return float(r)/(2.**18)

def frac2rank(f):
  x = abs(f)
  frac = x - float(int(x))
  xi = frac*(2.**18)
  if xi != float(int(xi)):
    print '%d frac2rank f=%g x=%g xi=%g'%(rank, f, x, xi)
    raise RunTimeError
  return int(xi)

def decode_vgap_val(v):
  r = frac2rank(v)
  sid = int(v)
  return (r, sid)

def pr(data, label):
  h.pc.barrier()
  for i in range(nhost):
    if i == rank:
      print '%d %s\n'%(rank,label),data
      h.pc.barrier()

def setup_transfer_verify():
  if rank == 0 : print 'setup_transfer_verify'
  h.finitialize(-65)
  frac = rank2frac(rank)
  for sec in h.allsec():
      sec.v = -1 - frac
  for seg in src2sids:
    seg.v = src2sids[seg][0] + frac
  for tar in tar2sid:
    tar.vgap = -2.0

  # do the parallel transfer
  h.finitialize()
  # note that FInitializeHandlers may destroy v but the transfer takes place
  # before any callback except type 3. So all the targets should have proper
  # value of firstsrcsid.rank

  # test 0. No transferred values are negative
  for tar in tar2sid:
    if tar.vgap < 0.0:
      print '%d %s sid=%d vgap=%g'%(rank, tar.hname(), tar2sid[tar], tar.vgap)
      raise RuntimeError
  # test 1. All the transferred values make sense in terms of rank
  for tar in tar2sid:
    if frac2rank(tar.vgap) >= nhost:
      print '%d %s has invalid rank code %d with value %g'%(rank, tar.hname(), frac2rank(tar.vgap), tar.vgap)
      raise RuntimeError

  # test 2. All the targets for a given sid should have the same value
  for sid in sid2tars:
    x0 = sid2tars[sid][0].vgap
    for tar in sid2tars[sid]:
      if tar.vgap != x0:
        print '%d %s %g != %g %s'%(rank, sid2tars[sid][0].hname(),x0, tar.vgap, tar.hname())
        raise RuntimeError

  # test 3. Send sid and vgap's sid back to rank it came from and verify on
  # the source rank that those sid's exist and have the same source
  # Because of test 2, only need to test first target of an sid
  data = []
  for i in range(nhost):
    data.append(None)
  for sid in sid2tars:
    r,ssid = decode_vgap_val(sid2tars[sid][0].vgap)
    if data[r] == None:
      data[r] = []
    data[r].append((sid, ssid))

  pr(data, 'source')
  data = h.pc.py_alltoall(data)
  pr(data, 'destination')

  for r,x in enumerate(data):
    if x:
      for pair in x:
        for sid in pair:
          if not sid2src.has_key(sid):
            print '%d target sid %d from %d not associated with source here'%(rank,sid,r)
            raise RuntimeError
