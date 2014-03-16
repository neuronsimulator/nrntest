#!/usr/bin/bash

run_from_stdin()
{
  nrniv -nobanner -isatty < $1
}

(
for i in test2.hoc test3.hoc test4.hoc ; do
  echo "begin run_from_stdin $i"
  run_from_stdin $i
  echo "begin nrniv < $i"
  nrniv -nobanner < $i
  echo "begin nrniv $i"
  nrniv -nobanner $i -c 'quit()'
done

for i in test2.py test6.py ; do
  echo "begin nrniv -python $i"
  nrniv -nobanner -python $i < /dev/null
done
) > temp.cmp 2>&1

diff test.cmp temp.cmp
