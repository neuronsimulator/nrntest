from neuron import *
'''
class MetaHocObject(type):
  ho = hoc.HocObject
  def __new__(cls, name, bases, attrs):
    #print cls, name, bases
    m = False
    for b in bases :
      if hasattr(b, '__mro__'):
        for bb in b.__mro__ :
          if bb == MetaHocObject.ho :
            if m == True:
              raise Exception("Inheritance of multiple HocObject not allowed")
            m = True
    return type.__new__(cls, name, bases, attrs)

def hclass(c):
    class hc(hoc.HocObject):
        __metaclass__ = MetaHocObject
        def __new__(cls, *args, **kwds):
            kwds.update({'hocbase':cls.htype})
            return hoc.HocObject.__new__(cls, *args, **kwds)
    setattr(hc, 'htype', c)
    return hc
'''

class A(hclass(h.Vector)): pass
a = A(5)

class B(hclass(h.List)): pass
b = B()

class C(object): pass

class D(): pass

class E(D, C, A): pass

class F(D, B, C, A): pass
