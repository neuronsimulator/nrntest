import neuron
h = neuron.h

soma = h.Section()
axon = h.Section()
axon.connect(soma)
dends = []
for i in range(3) :
  dends.append(h.Section())
  dends[i].connect(soma, 0)

h.topology()

sl = h.SectionList()
sl.wholetree()

for s in sl :
  print s

for s in h.allsec() :
  print s

dends[1].push() ; sr = h.SectionRef() ; h.pop_section()

sr.sec.push() ; print h.secname(), sr.sec, dends[1] ; h.pop_section()
print sr.sec == dends[1]
print sr.root == soma

soma.push() ; sr = h.SectionRef() ; h.pop_section()
print sr.nchild(), len(sr.child)
print sr.child[2] == dends[0]
for x in sr.child :
  print x

soma=0
dends=0
axon=0
h=0
sl=0
sr=0
x=0
s=0
i=0
