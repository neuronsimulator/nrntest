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

NEURON {THREADSAFE  GLOBAL usefac}
PARAMETER { usefac = 1 }
ASSIGNED {afac}
VERBATIM
extern int secondorder;
extern int cvode_active_;
ENDVERBATIM
PROCEDURE setfac() {
VERBATIM
	if (cvode_active_ || usefac==0.0) {
		afac = 1.0;
	}else if (secondorder == 0) {
		afac = 1.0/(1.0 + dt/tau);
	}else{
		afac = exp(-dt/2.0/tau);
	}
ENDVERBATIM
}


INITIAL {
	i = 0
	setfac()
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
	i = i - weight*afac
}

