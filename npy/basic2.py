import neuron
h = neuron.h

def hclass(c) :
  class hc(neuron.hoc.HocObject) :
    def __new__(cls, *args, **kwds) :
      kwds.update({"hocbase":cls.htype})
      #print ("__new__ ", cls, args, kwds)
      return neuron.hoc.HocObject.__new__(cls, *args, **kwds)
  setattr(hc, 'htype', c)
  return hc

class MyVector(hclass(h.Vector)) :
  y = "I am a MyVector"
  def pr(self) :
    print (self)
    print((self.size()))
    self.printf()


class MyList(hclass(h.List)) :
  def pr(self) :
    print (self)
    print((self.count()))


v = MyVector(4)
v.pr()
print((v.y))
l = MyList()
l.pr()

class My2Vector(MyVector) :
  y = "I am a My2Vector"
  z = ['one', 'two']
  x = "override x"
  def resize(self, n) :
    print((self, "resize to", n))
    neuron.hoc.HocObject.baseattr(self, 'resize')(n)

v = My2Vector(4)
print (v)
v.printf()
v.resize(2)
v.printf()
v.pr()
print((v.y))
print((v.z))
print((v.z[1]))
v.z[1] = 'three'
print((v.z[1]))
print((v.x))
print((v.x[1]))
v.z = "changed z"
print((v.z))
v.y = "changed y"
print((v.y))
v.x = 5
print((v.x))
zz = neuron.hoc.HocObject.baseattr(v, 'x')
print (zz)
neuron.hoc.HocObject.baseattr(v, 'x')[1] = .5
print((neuron.hoc.HocObject.baseattr(v, 'x')[1]))
v.printf()

print((v.x[1]))
