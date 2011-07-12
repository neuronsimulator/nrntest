NEURON {
	POINT_PROCESS ExpVSyn
}

UNITS {
	(mV) = (millivolt)
}

ASSIGNED { v(mV) }

NET_RECEIVE(weight (mV)) {
	v = v + weight
}

