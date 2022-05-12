#!/bin/sh

function run() {
	${MPIEXEC_NAME} -n $1 nrniv -nobanner -mpi -c nt=$2 -c cv=$3 ringpar.hoc
	sortspike out.dat temp
	diff ringpar_$3.dat temp
}

function series() {
	run 1 1 $1
	run 1 4 $1
	run 4 1 $1
	run 2 2 $1
}

# fixed step
series 0

#global variable
series 1

#local variable
series 2

