NEURON {
	POINT_PROCESS Destexhe
	NONSPECIFIC_CURRENT i
	GLOBAL Alpha, Beta, Rinf, Rtau, Rdelta
	RANGE synon, g, Erev, gmax
}

UNITS {
	(mV) = (millivolt)
	(uS) = (micromho)
	(nA) = (nanoamp)
}

PARAMETER {
	Alpha = 2 (1/ms)
	Beta = 10 (1/ms)
	Cdur = 1 (ms)
	Erev = 0 (mV)
	gmax = .001 (uS)
}

ASSIGNED {
	i (nA)
	v (mV)
	Rdelta
	Rinf
	Rtau (ms)
	synon
	g (uS)
}

STATE {Ron Roff}

INITIAL {
    Ron = 0   Roff = 0
    Rinf = Alpha / (Alpha + Beta)
    Rtau = 1 / (Alpha + Beta)
    Rdelta = Rinf*(1 - exp(-Cdur/Rtau))
    synon = 0
}

BREAKPOINT {
    SOLVE release METHOD cnexp
    g = gmax*(Ron + Roff)
    i = g*(v - Erev)
}

DERIVATIVE release {
    Ron' = (synon*Rinf - Ron)/Rtau
    Roff' = -Beta*Roff
}

NET_RECEIVE(weight) {
    if (flag == 0) { : spike - T on
        synon = synon + weight
        net_send(Cdur, 1)
    }else{ : transmitter off
        synon = synon - weight
        Ron = Ron - weight*Rdelta
        Roff = Roff + weight*Rdelta
    }
}
