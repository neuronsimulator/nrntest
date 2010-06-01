import hoc
h  = hoc.HocObject()
h('obfunc newlist() { return new List() }')
list = h.newlist()
apnd = list.append
apnd([1,2,3])
apnd(('a', 'b', 'c'))
apnd({'a':1, 'b':2, 'c':3})
item = list.object
for i in range(0, int(list.count())) :
  print item(i)

h('for i=0, List[0].count-1 print List[0].object(i)')

