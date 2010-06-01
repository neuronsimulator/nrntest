from neuron import h
h('obfunc newvec() { return new Vector($1) }')
h('''proc change() { \
  printf("enter %g %s %s\\n", $&1, $o2, $s3) \
  $&1 = 2 \
  $o2 = new List() \
  $s3 = "goodbye" \
}''')
h('strdef hs')
h('objref ho')
h('hx = 0')

h.hs = 'hello'
h.hx = 1

h('change(&hx, ho, hs)')
print h.hx, h.ho, h.hs




h('load_file("nrngui.hoc")')
h('obfunc hocstring() { return new String($s1) }')
s = h.hocstring('hello world')
h.xpanel("test1")
h.xvarlabel(s.s)
h.xpanel()

h('strdef ss')
h('ss = "hello world"')
h.xpanel("test2")
h.xvarlabel(h.ss)
h.xpanel()
