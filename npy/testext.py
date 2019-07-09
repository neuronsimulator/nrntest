from neuron import h
h('load_file("nrngui.hoc")')
#h('load_file("hh.ses")')

import threading
import time
def f() :
  #h.doEvents()
  h.doNotify()
  #print "timer"

class LoopTimer(threading.Thread) :
  """
  a Timer that calls f every interval
  """
  def __init__(self, interval, fun) :
    """
    @param interval: time in seconds between call to fun()
    @param fun: the function to call on timer update
    """
    self.interval = interval
    self.fun = fun
    threading.Thread.__init__(self)
    self.setDaemon(True)

  def run(self) :
    while True:
      self.fun()
      time.sleep(self.interval)

timer = LoopTimer(.05, f)
timer.start()
print("hello")
