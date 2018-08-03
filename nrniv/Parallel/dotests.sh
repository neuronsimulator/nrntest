#!/bin/bash

err=0

files="alltoall.py alltoall_dict.py"

arg=""
osname=`uname -s`
if test "$osname" = "Darwin" ; then
  arg="--oversubscribe"
fi

echo $files $np

function f() {
  echo "hello $1"
  a=`mpiexec $arg -n 4 nrniv -nobanner -mpi -python $1 2>/dev/null | sed -n '$p'`
  if test "$a" != 0 ; then
    echo "$1 failed"
    err=1
  else
    echo "$1 succeeded"
  fi
  exit $err
}

for i in $files ; do
 echo $i
 f $i
done

cd pargap
nrnivmodl
i=msgap.py
a=`mpiexec -n 2 nrniv -nobanner -mpi -python $i |sed -n '$p'`
f

