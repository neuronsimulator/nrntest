#!/bin/sh
NRN="$HOME/neuron/nrnmpi/x86_64/bin/nrniv"
run() {
	rm out*.dat
	$NRN $2.hoc
	for j in out*.dat; do
		cmp $j $1dat/$j
	done
	rm out*.dat
	${MPIEXEC_NAME} -np $3 $NRN -mpi $2.hoc >/dev/null
	for j in out*.dat; do
		cmp $j $1dat/$j
	done
}

run ms2 ms2short 3
run ms2 ms2rt 3
run ms3 ms3 4
run ms4 ms4 5
run ms5 ms5 6
run ms6 ms6 5
run ms7 ms7 5
#run ms8 ms8 4 # compare out3.dat and out4.dat
