#!/bin/bash

err=0

files=("alltoall.py" "alltoall_dict.py" "collective.py" "pargap/msgap.py")
nrnivmodl pargap

function f() {
  echo "Running nrniv/Parallel/${1}"
  a=$(mpiexec ${MPIEXEC_OVERSUBSCRIBE---oversubscribe} -n 4 nrniv -nobanner -mpi -python $1 2>/dev/null | sed -n '$p')
  echo "${1} stdout: ${a}"
  if test "$a" != 0 ; then
    echo "$1 failed"
    err=1
  else
    echo "$1 succeeded"
  fi
  
}

for i in ${files[@]}; do
 f $i
done
exit $err

