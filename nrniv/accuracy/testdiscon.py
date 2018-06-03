# stdbuf -i0 -o0 -e0 python testdiscon.py &> result
# unbuffering stdout and stderr nicely interleaves output to file
# Tests accuracy of POINT_PROCESS models with NET_RECEIVE
# with nrn_netrec_state_discon equal 0 and 1 and
# secondorder equal 0 and 2.  Order statistics summarized at end.

from neuron import h, gui
import math

use_voltage_clamp = False

def uses_pointer(mechname):
  # do not get involved with POINTER
  ms = h.MechanismStandard(mechname, 0)
  for i in range(int(ms.count())):
    n = h.ref("")
    ms.name(n, i)
    if ms.get(n[0]) == -1e+300:
      return True
  return False



class Model():
  def __init__(self, mechname):
    #set variables in case of exception so that __del__ still works.
    self.nc = None
    self.stim = None
    self.syn = None
    self.vc = None
    self.s = None

    self.mechname = mechname
    constructor = h.__getattribute__(mechname)
    self.soma = h.Section(name='soma')
    s = self.soma
    s.L = 10.
    s.diam = 10./h.PI
    s.insert('pas')
    seg = s(0.5)
    seg.e_pas = -65.0
    seg.g_pas = 0.0001

    self.syn = constructor(seg)
    self.stim = h.NetStim()
    self.stim.number = 2
    self.stim.interval = 5
    self.stim.start = 1

    self.nc = h.NetCon(self.stim, self.syn)
    self.nc.delay = 1
    self.nc.weight[0] = .001

    if use_voltage_clamp:
      self.vc = h.SEClamp(seg)
      self.vc.amp1 = -65.0
      self.vc.dur1 = 1e9

  def __del__(self):
    # proper order for destruction
    self.nc = None
    self.stim = None
    self.syn = None
    self.vc = None
    self.s = None

  def gui(self):
    self.g = h.Graph()
    self.g.size(0, h.tstop, -65, -50)

  def run(self):
    self.gui()
    self.g.label(0.1, 0.9, self.mechname, 2)
    self.g.label("secondorder=%g"%h.secondorder)
    self.g.label("dt=%g"%h.dt)
    vvec = h.Vector()
    tvec = h.Vector()
    if use_voltage_clamp:
      vvec.label("ic")
      vvec.record(self.syn, self.vc._ref_i, 0.1)
    else:
      vvec.label("v")
      #vvec.record(self.syn, self.soma(.5)._ref_v, 0.1)
      vvec.record(self.syn, self.syn._ref_A_AMPA, 0.1)
    tvec.record(self.syn, h._ref_t, 0.1)
    h.cvode.atol(1e-10)

    # cvode is standard but use first result to change weight so that
    # there is a substantial synaptic change
    dtsav = h.dt
    try:
      h.cvode_active(1)
      h.run()
    except:
      h.cvode_active(0)
      h.dt/=1000 
      print ("cvode failed so try fixed step dt=%g as standard"%h.dt)
      h.run()
    sz = 10*h.tstop
    scale = (vvec.max(10, sz) - vvec.min(10, sz))/10.
    print ("scale=%g"%scale)
    if abs(scale) > 1e-6:
      self.nc.weight[0] /= scale
    elif math.isnan(scale) or abs(scale) > 1e6:
      print ("numerical problem")
    else:
      print ("No response")
    h.run()
    h.dt = dtsav
    vvec.resize(sz)
    tvec.resize(sz)
    vvec.line(self.g, tvec, 1, 3)
    vstd = vvec.c()
    tstd = tvec.c()
    vmag = vvec.c().sub(vvec.x[10]).abs().sum()
    

    result = []
    h.cvode_active(0)
    for adjust in [0, 1]:
      h.nrn_netrec_state_adjust = adjust
      color = 3 if adjust is 1 else 2
      for dt in [h.dt/8, h.dt/4, h.dt/2, h.dt]:
        h.dt = dt
        h.run()
        vvec.resize(sz)
        tvec.resize(sz)
        vvec.line(self.g, tvec, color, 1)
        vdif = vvec.c().sub(vstd).abs().sum()
        tdif = tvec.c().sub(tstd).abs().sum()
        result.append((self.mechname, h.secondorder, adjust, dt, vdif, tdif, vmag))
        print ("%s %g %g %g %g %g" % result[-1][:-1])

      h.nrn_netrec_state_adjust = 0

    self.g.exec_menu("View = plot")
    return result

def one(mechname):
  m = Model(mechname)
  if 'ProbAMPANMDA_EMS'in  mechname:
    m.syn.setRNG(3,1)
  h.psection()
  dtsav = h.dt
  try:
    result = m.run()
  except:
    print ( "%s run failed, ignore result"%mechname)
    result = None
  h.dt = dtsav
  return m, result

def all(substring, start=0, end=-1):
  results = []
  mt = h.MechanismType(1)
  cnt = int(mt.count())
  end = cnt if end == -1 or end > cnt else end
  for i in range(start, end):
    if mt.is_netcon_target(i) and not mt.is_artificial(i):
      mt.select(i)
      n = h.ref("")
      mt.selected(n)
      mechname = n[0]
      if substring not in mechname:
        continue
      if uses_pointer(mechname):
          print ("\n%d> %s has a POINTER"%(i, mechname))
          if 'ProbAMPANMDA_EMS' not in  mechname:
            continue
      print ("\n%d of %d"%(i, cnt))
      print (mechname)
      for h.secondorder in [0, 2]:
        m, result = one(mechname)
        if cnt > 30:
          m.g = None
        if result:
          results.append((i, result, m.g))
        del m
  h.secondorder = 0
  return results

def order(item, r, so):
    mechname, secondorder, adjust, dt, vdif, tdif, vmag = r[0]
    transpose = list(map(list, zip(*r)))
    e = transpose[4][4:] # vdiff with adjust
    e0 = transpose[4][:4] # vdiff without adjust
    o = []
    if e[0] > 0.:
      for i in range(1, len(e)):
        o.append(int(round((e[i]/e[i-1])/2)))
      o = o[0] if o[1:] == o[:-1] else o
      if secondorder is so:
        if so is 0:
          print ("%d: %s order %s  enorm %g   %g"%(item, mechname, str(o), e[3]/vmag, e0[3]/vmag))
        else:
          print ("%d: %s order %s  enorm %g"%(item, mechname, str(o), e[3]/vmag))


if __name__ == '__main__':
  h.tstop=10
  if False:
    m, result = one('RampSyn')
    g = m.g

    h.secondorder=2
    m.run()
  else:
    results = all("ProbAMPA", start=0, end=-1)
    for so in [0, 2]:
      print ("\nsecondorder=%d"%so)
      for r in results:
        order(r[0], r[1], so)
