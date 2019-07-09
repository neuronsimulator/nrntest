from neuron import h, gui
from e import e

s = h.Section()
s.insert('hh')

iname = s.hoc_internal_name()
print(iname)
exec('s2 = h.' + iname)
print('s is s2', s is s2)
print('s is h.cas()', s is h.cas())
print('s == h.cas()', s == h.cas())

h('create soma')
s4 = h.soma
print(s4.hoc_internal_name())
exec('s5 = h.' + s4.hoc_internal_name())
print('s5 is s4', s5 is s4)
print('s5 == s4', s5 == s4)
print(s5.name())
s6 = h.Section(name="s6")
s6.name()
h.topology()

h('''__nrnsec_0x { print secname() }''')
e('s7 = h.__nrnsec_0x')
h('''__nrnsec_0xaaaa { print secname() }''')
e('s7 = h.__nrnsec_0xaaaa')

del(s)
print(s2)
print(s2.name())
sn = 'print h.'+ s2.hoc_internal_name() + '.L'
e(sn)
del(s2)
e(sn)

