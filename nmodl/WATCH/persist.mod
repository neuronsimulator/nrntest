: can several thresholds be watched in a POINT_PROCESS?

NEURON {
	POINT_PROCESS Persistent
	RANGE th1, th2, th3
}
UNITS { (mV) = (millivolt) }
PARAMETER { th1 = -50(mV)  th2 = -40(mV)  th3 = -30(mV) }
ASSIGNED { v (mV)}

INITIAL {
	net_send(0, 1)
}

NET_RECEIVE(w) {
	: note that the conditions are persistent
	if (flag == 1) {
		WATCH (v > th1) 2
		WATCH (v > th2) 3
		WATCH (v < th3) 4
	}else if (flag != 0) {
		UNITSOFF printf("t=%g v=%g flag=%g\n", t, v, flag) UNITSON
	}
}
