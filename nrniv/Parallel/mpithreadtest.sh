#!/bin/sh

function niv() {
	mpiexec -np $1 nrniv -mpi -nobanner -c nt=$2 -c s=$3 -c cv=$4 mpithreadtest.hoc
}

function run() {
	niv $1 $2 $3 $4
	for i in out*.dat ; do cmp $i tmp/$i ; done
}

function series() {
	niv 1 1 0 $1
	mv out*.dat tmp
	run 1 1 1 $1
	run 1 4 1 $1
	run 4 1 1 $1
}
	
#fixed step
series 0
run 2 2 1 0

#global variable step
series 1
#run 2 2 1 1 #not allowed
