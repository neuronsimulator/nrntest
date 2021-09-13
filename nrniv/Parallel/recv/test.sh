#!/bin/sh

NRN="$HOME/neuron/nrnmpi/x86_64/bin/nrniv"

run() {
	rm -f temp1 temp2 temp3 temp4 recv.dat out.dat
	ct="celltype=$1"
	echo "$ct $2"
	$NRN -nobanner -c "$ct" -c "{$2}" init.hoc > /dev/null
	./sortrecv recv.dat temp1
	cmp temp1 recv$1.std
	sortspike out.dat temp2
	cmp temp2 out$1.std
	rm -f recv.dat out.dat
	echo "mpi $ct $2"
	mpiexec --oversubscribe -n 4 $NRN -mpi -nobanner -c "$ct" -c "{$2}" init.hoc > /dev/null
	./sortrecv recv.dat temp3
	cmp temp3 temp1
	sortspike out.dat temp4
	cmp temp4 temp2
}

run 1 ""
run 1 "spkbufsize=5"
run 1 "binqueue=1"
run 1 "selfqueue=1"
run 1 "spkbufsize=1 binqueue=1"
run 1 "spkbufsize=1 binqueue=1 selfqueue=1"

#run 0 ""
#run 0 "spkbufsize=5"
run 0 "binqueue=1"
#run 0 "selfqueue=1"
run 0 "spkbufsize=1 binqueue=1"
run 0 "spkbufsize=1 binqueue=1 selfqueue=1"


