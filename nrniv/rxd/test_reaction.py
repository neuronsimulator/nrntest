from neuron import h

soma = h.Section()

sl = h.SectionList()
sl.append(sec=soma)

ca = h.Diffusible('ca', sl)
na = h.Diffusible('na', sl)
k = h.Diffusible('k', sl)
cl = h.Diffusible('cl', sl)

r1 = h.Reaction('k', '5*ca+sin(na/ca)')
r2 = h.Reaction('cl', 'cl*na/k-ca')

for r in [r1, r2]:
    print 'created a reaction changing', r.state_var(), 'and depending on the state variables:',
    print ', '.join(r.var(i) for i in xrange(int(r.n_var())))
