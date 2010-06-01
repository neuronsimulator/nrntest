NEURON {
	SUFFIX f2e
	POINTER pin, pout
	RANGE fac
}

PARAMETER {fac = 0}
ASSIGNED {pin pout}

BEFORE BREAKPOINT {
	pout = fac * pin
}

