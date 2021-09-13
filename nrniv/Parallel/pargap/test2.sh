#!/bin/sh

function niv() {
	mpiexec --oversubscribe -np $1 nrniv -mpi -nobanner -c nt=$2 -c cv=$3 test2.hoc
}

function run() {
	niv $1 $2 $3
	sortspike out.dat temp1
	cmp temp temp1
}

function series() {
	niv 1 1 $1
	sortspike out.dat temp
	run 1 4 $1
	run 4 1 $1
}
	
#fixed step
series 0
#run 2 2 0

#global variable step
series 1
#run 2 2 0 #not allowed
