from neuron import h

from e import e

def test(fname):
  # file as string without the ^D
  global b
  b = open(fname).read().replace("\x04\n", "")

  # zzz replaced by fname below
  a = '''
h('xopen("zzz")')
h.xopen('zzz')
h.execute('xopen("zzz")')
h.execute1('xopen("zzz")')
h.load_file('zzz')
h(b)
h.execute(b)
h.execute1(b)
'''
  a = a.replace("zzz", fname)

  for line in a.splitlines():
    print "TEST"
    if len(line):
      e('z = ' + line + '; print "result=",z')

test("test2.hoc")
test("test3.hoc")

quit()
