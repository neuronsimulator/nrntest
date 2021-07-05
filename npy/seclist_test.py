from neuron import h
soma = h.Section(name='soma')
dend = h.Section(name='dend')
mylist2 = h.SectionList([soma, dend])
sec = dend
del dend
for sec in mylist2:
    print(sec)

del soma
del sec

def test(n=100):
  slist = [h.Section(name='s%d'%i) for i in range(n)]
  sl = h.SectionList(slist)
  import random
  random.shuffle(slist)

  while len(slist):
    slist = slist[10:]
    for sec in sl:
      pass
    sec = None
  m=0
  for sec in sl:
    print(sec)
    m += 1
  print (m == 0)

for i in range(5):
  test(100)

