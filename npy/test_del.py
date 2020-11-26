# It is now the case that h.delete_section(python_section) is allowed.
# In this case the PythonSection object retains a reference to the invalid
# Section and is a zombie.
# Also SectionRef.unname() and SectionRef.rename('name') for PythonSection
# does nothing and returns 0.0.

from neuron import h

def test():
    sec = h.Section(name='dend')

    for sec in h.allsec():
        h.disconnect(sec=sec)
        sref = h.SectionRef(sec=sec)
        #defeated the guards against deleting the Section pointed to by
        # a PythonSection
        sref.rename('delete')
        h.disconnect(sec=sec)
        #used to be allowed only for hoc sections (create ...)
        h.delete_section(sec=sec)

test()  # works

test() # originally caused a segfault.

def testsz(n):
    for i in range(n):
        test()

# verify that we are not leaking memory
def testmemleak(n, m):
    sz = h.nrn_mallinfo(1)
    for i in range(n):
        testsz(m)
        sz1 = h.nrn_mallinfo(1) - sz
        print("%d %d size=%d" %(i, m, sz1))

testmemleak(10, 100)


