#!/bin/sh
# try:
# sh alltest.sh >& tempx
# sed 's/0x[0-9a-f]*/0x.../g' tempx > tempy
# sed 's/0x[0-9a-f]*/0x.../g' alltest.stdouterr > tempz
# diff tempz tempy
# And ignore print parentheses (python2) and timing.

for i in allsec.py cvevent.py ; do
  echo $i
  echo 'quit()' | neurondemo -nobanner -python $i
done

PY=`ls *.py`

for i in $PY ; do
  echo $i
  echo 'quit()' | nrniv -nobanner -python $i
done


