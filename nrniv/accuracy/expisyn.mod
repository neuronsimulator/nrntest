NEURON {
	POINT_PROCESS ExpISyn
	RANGE tau, i
	NONSPECIFIC_CURRENT i
}

UNITS {
	(nA) = (nanoamp)
	(mV) = (millivolt)
}

PARAMETER {
	tau = 0.1 (ms) <1e-9,1e9>
}

STATE {
	i (nA)
}

INITIAL {
	i = 0
}

BREAKPOINT {
	SOLVE state METHOD cnexp
:	printf("BREAKPOINT t=%g i=%g\n", t, i)
}

DERIVATIVE state {
	i' = -i/tau
:	printf("DERIVATIVE t=%g i=%g\n", t, i)
}

NET_RECEIVE(weight (nA)) {
:        printf("NET_RECEIVE t = %f, i = %f - (weight = %f)\n", t, i, weight)
	i = i - weight
}

