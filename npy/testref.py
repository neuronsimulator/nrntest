import neuron
h = neuron.h

h('proc chx() { $&1 = 2 }')
h('proc chstr() { $s1 = "goodbye" }')
h('proc chobj() { $o1 = new List() }')

y = h.ref(5)
print y
h.chx(y)
print y
print y[0]
y[0] = 3
print y[0]

y = h.ref("hello")
print y
h.chstr(y)
print y
print y[0]
y[0] = "another"
print y[0]

y = h.ref([1,2,3])
print y
h.chobj(y)
print y
print y[0]
y[0] = [1,2,3]
print y[0]
