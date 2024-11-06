#!/usr/bin/env bash

set -u

err=0

files=("alltoall.py" "collective.py" "pargap/msgap.py")
nrnivmodl pargap

run_neuron() {
    echo "Running nrniv/Parallel/${1}"
    output="$(mpiexec ${MPIEXEC_OVERSUBSCRIBE---oversubscribe} -n 4 nrniv -nobanner -mpi -python "$1" 2>/dev/null | sed -n '$p')"
    echo "${1} stdout: ${output}"
    if test "${output}" != 0; then
        echo "$1 failed"
        err=1
    else
        echo "$1 succeeded"
    fi

}

for path in ${files[@]}; do
    run_neuron "${path}"
done

exit $err
