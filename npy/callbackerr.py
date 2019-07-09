from neuron import h
h.load_file('nrngui.hoc')

def callback1(tol=0.01):
  print("callback1: t=%s" % h.t)
  1/0
  print("I just made a divide-by-zero error")
  interval = 10000
  print("next callback1 at %s" % (h.t+interval))
  h.cvode.event(h.t + interval, callback1)
  #return(interval)

h.cvode_active(1)
fih = h.FInitializeHandler(callback1)
h.stdinit()
h.cvode.solve(50000)

