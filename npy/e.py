from __main__ import *
import sys
def e(stmt) :
  try:
    print stmt
    exec(stmt)
  except:
    print sys.exc_info()[0], ': ', sys.exc_info()[1]

