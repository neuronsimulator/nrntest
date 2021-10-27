#!/bin/bash

nrnivmodl

ERR=0

run() {
	rm -f recv$1.dat* out$1.dat* recv.dat out.dat
	ct="celltype=$1"
	echo "run with -> $ct $2 <-"
	nrniv -nobanner -nogui -c "$ct" -c "{$2}" init.hoc > /dev/null
	./sortrecv recv.dat recv$1.dat.sorted
	cmp recv$1.dat.sorted recv$1.std
	if [ $? -ne 0 ]; then
		ERR=1
	fi
	sortspike out.dat out$1.dat.sorted
	cmp out$1.dat.sorted out$1.std
	if [ $? -ne 0 ]; then
		ERR=1
	fi
	rm -f recv.dat out.dat

	RUN_WITH_MPI="${have_nrnmpi-yes}"
	if [ "${RUN_WITH_MPI}" = "yes" ] ; then
		echo "run with mpi -> $ct $2 <-"
		mpiexec ${MPIEXEC_OVERSUBSCRIBE---oversubscribe} -n 4 nrniv -mpi -nobanner -nogui -c "$ct" -c "{$2}" init.hoc > /dev/null
		./sortrecv recv.dat recv$1.dat.sorted.mpi
		cmp recv$1.dat.sorted.mpi recv$1.dat.sorted
		if [ $? -ne 0 ]; then
			ERR=1
		fi
		sortspike out.dat out$1.dat.sorted.mpi
		cmp out$1.dat.sorted.mpi out$1.dat.sorted
		if [ $? -ne 0 ]; then
			ERR=1
		fi
	else
		echo "run with mpi is DISABLED-> $ct $2 <-"
	fi
	
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

exit $ERR
