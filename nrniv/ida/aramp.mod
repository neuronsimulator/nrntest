NEURON {
	POINT_PROCESS RampFunc
	RANGE del, dur, amp0, slope
	RANGE x
}

UNITS { (mV) = (millivolt) }

PARAMETER {
	del = 0 (ms)
	dur = 0 (ms)
	amp0 = 0 (1)
	slope = 0 (1/ms)
}

ASSIGNED { on (1) x (1) }

INITIAL {
	if (dur > 0) {
		net_send(del, 1)
	}
	x = 0
	on = 0
}

BEFORE BREAKPOINT {
	x = on*(amp0 + slope*(t - del))
	:printf("aramp t=%.15g x=%.15g\n", t, x)
}

NET_RECEIVE(w) {
	if (flag == 1) {
		on = 1
		net_send(dur, 2)
	}else if (flag == 2) {
		on = 0
	}
}

