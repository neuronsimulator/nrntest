NEURON {SUFFIX test}

ASSIGNED { area	}
	
BREAKPOINT {
    VERBATIM
        printf("Area from MOD: %g \n", area);
    ENDVERBATIM
}
