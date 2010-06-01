from hoc import execute
execute('load_file("nrngui.hoc")')

secnames = []

execute('''
create soma, axon, dend[3]
strdef str
forall { \
  sprint(str, "secnames.append('%s')", secname()) \
  nrnpython(str) \
}
''')

print secnames

