#!/bin/bash

err=0

i=alltoall.py

a=`mpiexec -n 4 nrniv -nobanner -mpi -python $i |sed -n '$p'`

f() (
  if test "$a" != 0 ; then
    echo "$i failed"
    err=1
  else
    echo "$i succeeded"
  fi
  exit $err
)

f

cd pargap
nrnivmodl
i=msgap.py
a=`mpiexec -n 2 nrniv -nobanner -mpi -python $i |sed -n '$p'`
f

