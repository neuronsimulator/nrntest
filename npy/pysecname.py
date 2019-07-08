''' wish to have python section names that can be used with NEURON's
classical GUI and persist across launches so ses files are valid
'''

from neuron import h, gui

soma = h.Section(name="soma")
dend = h.Section(name="dend")
dend.connect(soma(1))

aden = [h.Section(name="aden[%d]"%i) for i in range(4)]

axon = h.Section()
axon.connect(soma(0))

h('create apical')
h.apical.connect(soma(.5))

s = h.ref("")
for sec in h.allsec():
  h.sectionname(s)
  print (sec.name(), s[0], h.secname(1), sec.hoc_internal_name())

h('''forall print secname(), " ", secname(1)''')

names = [h.secname(1) for _ in h.allsec()]

for s in names:
  h('%s print "hoc ", secname(1)'%s)

if False: # direct Python access to h._pysec.name does not work
  for s in names:
    print ("h.%s"%s + ".name()")
    print ("python %s %s"% (s, eval("h.%s"%s + ".name()")))

h.load_file("pysecname.ses")
