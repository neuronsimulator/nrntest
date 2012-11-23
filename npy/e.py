import __main__
import sys
def e(stmt) :
  try:
    print stmt
    exec stmt in __main__.__dict__
  except:
    print sys.exc_info()[0], ': ', sys.exc_info()[1]

