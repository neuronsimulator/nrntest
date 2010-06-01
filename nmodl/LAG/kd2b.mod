: HH voltage-gated potassium current

NEURON {
	SUFFIX kd2b                      : changed the name of the file here to kd2b
	USEION k READ ek WRITE ik
	RANGE gkbar, gk, ik, vlag
}

UNITS {
	(S)  = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER { 
	gkbar = 0.036 (S/cm2)
	a = 0.0189324 (/ms)
	b = -4.18371 (mV)
	c = 6.42606 (mV)
	d = 0.015857 (/ms)
	e = 25.4834 (mV) 
	delay = .3 (ms)
}

ASSIGNED {
	v (mV)
	ek (mV) : typically ~ -77.5
	ik (mA/cm2)
	gk (S/cm2)
	vlag (mV)
	vsav (mV)
}

STATE { n }


BREAKPOINT {
	SOLVE states METHOD cnexp
	gk = gkbar * n                : changed to single gating particle
	ik = gk * (v - ek)
}

INITIAL {
	: Assume v has been constant for a long time
	n = alpha(v)/(alpha(v) + beta(v))
	f_vlag()
}

FUNCTION f_vlag() {
	vsav = v : need different pointers for each instance
	LAG vsav BY delay
	f_vlag = lag_vsav_delay
}

DERIVATIVE states {
	vlag = f_vlag()
	: Computes state variable n at present v & t
	n' = (1-n)*alpha(vlag) - n*beta(vlag)
}

FUNCTION alpha(Vm (mV)) (/ms) {
	alpha = a*(-(Vm+b))/(exp(-(Vm+b)/c)-1)              : 0.0189324*(-(v+-4.18371))/(exp(-(v+-4.18371)/6.42606)-1)     
}

FUNCTION beta(Vm (mV)) (/ms) {
	beta = d*exp(-Vm/e)      : 0.015857*exp(-v/25.4834)
}
