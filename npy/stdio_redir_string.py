from neuron import h

from cStringIO import StringIO
import sys

old_stderr = sys.stderr
sys.stderr = mystderr = StringIO()

status = h.load_file("test.hoc")

sys.stderr = old_stderr

if status == 0:  
  print ("load_file failed. Following is contents of mystderr.getvalue()...")
  print (mystderr.getvalue())
