NEURON {
	POINT_PROCESS Foo
	USEION na READ ena WRITE ina
	RANGE g
}

PARAMETER {
	g=0 (micromho)
}
ASSIGNED {
	ena (millivolt)
	ina (nanoamp)
}

BREAKPOINT {
	ina = g*(v - ena)
}
