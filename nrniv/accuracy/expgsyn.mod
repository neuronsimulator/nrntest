NEURON {
	POINT_PROCESS ExpGSyn
	RANGE tau, e, i, fac
	NONSPECIFIC_CURRENT i
	GLOBAL usefac
}

UNITS {
	(nA) = (nanoamp)
	(mV) = (millivolt)
	(uS) = (microsiemens)
}

PARAMETER {
	tau = 0.1 (ms) <1e-9,1e9>
	e = 0	(mV)
	usefac = 1
}

ASSIGNED {
	v (mV)
	i (nA)
	fac
}

STATE {
	g (uS)
}

VERBATIM
extern int secondorder;
extern int cvode_active_;
ENDVERBATIM
FUNCTION setfac(rate) {
VERBATIM
	if (cvode_active_ || usefac==0.0) {
		_lsetfac=1.0;
	}else if (secondorder == 0) {
		/*_lsetfac = exp(-_lrate*dt);*/
		_lsetfac = 1.0/(1.0 + _lrate*dt);
	}else{
		_lsetfac = exp(-_lrate*dt/2);
	}
ENDVERBATIM
}

INITIAL {
	g=0
	fac = setfac(1/tau)
}

BREAKPOINT {
	SOLVE state METHOD cnexp
	i = g*(v - e)
}

DERIVATIVE state {
	g' = -g/tau
}

NET_RECEIVE(weight (uS)) {
	g = g + weight*fac
}