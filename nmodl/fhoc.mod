:call a hoc function from a mod function
NEURON { SUFFIX nothing }

VERBATIM
static Symbol* fhoc_;
ENDVERBATIM

FUNCTION fmd(a, b) {
	LOCAL x
VERBATIM
{
	if (!fhoc_) {
		fhoc_ = hoc_lookup("fhoc");
	}
	hoc_pushx(_la);
	hoc_pushx(_lb);
	_lx = hoc_call_func(fhoc_, 2);
}
ENDVERBATIM
	fmd = x
}
