#!/bin/sh

for i in allsec.py cvevent.py ; do
  echo $i
  echo 'quit()' | neurondemo -python $i
done

PY=`ls *.py`

for i in $PY ; do
  echo $i
  echo 'quit()' | nrniv -python $i
done


