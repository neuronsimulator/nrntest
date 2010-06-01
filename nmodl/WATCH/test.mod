: can several thresholds be watched in a POINT_PROCESS?

NEURON {
	POINT_PROCESS Test
	RANGE th1, th2, vnext, del
}

PARAMETER { th1 = -50  th2 = -40 }
ASSIGNED { v vnext del}

INITIAL {
	net_send(0, 1)
}

NET_RECEIVE(w) {
	: note that the conditions are persistent
	if (flag == 1) {
		WATCH (v > th1) 2
		WATCH (v > th2) 3
		WATCH (v < 20) 4
	}else if (flag != 0) {
		printf("t=%g v=%g flag=%g\n", t, v, flag)
	}
	if (flag == 4) {
		vnext = v - 10
		del = 10
		WATCH (v < vnext - del) 6
		WATCH (v < vnext) 5
	}
	if (flag > 4) {
		vnext = v - 10
		del = del/10
		WATCH (v < vnext - del) 6
		WATCH (v < vnext) 5
	}
}
