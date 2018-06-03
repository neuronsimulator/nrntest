NEURON {SUFFIX test}

UNITS {
  FARADAY = (faraday) (coulombs)
  R = (R) (joule/degC)
  R1 = (k-mole) (joule/degC)
}

ASSIGNED { area	}
	
BREAKPOINT {
    VERBATIM
        printf("Area from MOD: %g \n", area);
    ENDVERBATIM
}

PROCEDURE p() {
  printf("mod UNITS FARADAY=%.12g  R=%.12g R(from k-mole)=%.12g\n", FARADAY, R, R1)
}
