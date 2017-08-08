NEURON {
	POINT_PROCESS RampSyn
	RANGE dur, e, i
	NONSPECIFIC_CURRENT i
}

UNITS {
	(nA) = (nanoamp)
	(mV) = (millivolt)
	(uS) = (microsiemens)
}

PARAMETER {
	dur = 2 (ms) <1e-9,1e9>
	e = 0	(mV)
}

ASSIGNED {
	v (mV)
	i (nA)
	m (uS/ms)
}

STATE {
	g (uS)
}

INITIAL {
	g=0
	m = 0
}

BREAKPOINT {
	SOLVE state METHOD cnexp
	i = g*(v - e)
:printf("BREAKPOINT t=%g g=%g v=%g i=%g\n", t, g, v, i)
}

DERIVATIVE state {
	g' = -m
:printf("DERIVATIVE t=%g g=%g\n", t, g)
}

NET_RECEIVE(weight (uS)) {
:printf("NET_RECEIVE g = %g + weight=%g\n", g, weight)
	if (flag == 0) {
		m = (g+weight)/dur
		g = g + weight
		net_send(dur, 1)
	}else{
		m = 0
		g = 0
	}	
}
