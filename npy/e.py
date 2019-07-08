import __main__
import sys
def e(stmt) :
  try:
    print(stmt)
    exec(stmt, __main__.__dict__)
  except:
    print(str(sys.exc_info()[0]) + ': ' + str(sys.exc_info()[1]))

