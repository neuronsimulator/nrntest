from neuron import h, gui
h('create axon')
import __main__
import sys
def e(stmt) :
  try:
    print stmt
    exec stmt in __main__.__dict__
  except:
    print sys.exc_info()[0], ': ', sys.exc_info()[1]

e('print h.axon.i_membrane_')
e('print h.axon(.5).i_membrane_')

h.delete_section()

h.load_file("imemaxon2.hoc")
for seg in h.axon:
  print seg.x, seg.i_membrane*seg.area()*(0.01), seg.i_membrane_
for seg in h.axon.allseg():
  print seg.x, seg._ref_i_membrane_[0], seg.i_membrane_

print h.axon.i_membrane, h.axon(.5).i_membrane
print h.axon.i_membrane_


