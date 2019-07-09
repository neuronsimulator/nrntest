import hoc
h = hoc.HocObject()
h("objref o1, o2, nil")
h.o1 = [1,2,3]
h.o2 = h.o1
h.o2 = h.o1
h.o2 = h.o1
h.o2 = h.o1
h.o2 = h.o1
h.o2 = h.o1
print(h.nil)
h.o2 = None
h.o1 = h.nil
