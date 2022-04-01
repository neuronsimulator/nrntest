NEURON {
	POINT_PROCESS ExpSynRecv
	RANGE tau, e, i
	NONSPECIFIC_CURRENT i
	POINTER vecs
	RANGE  ninput : count number of spikes coming in
	RANGE gid
}

PARAMETER {
	tau = 5 (ms)   <1e-9,1e9>
	e = 0 (millivolt)
}

ASSIGNED {
	v (millivolt)
	i (nanoamp)
	ninput
	gid vecs
}

STATE {
	g (microsiemens)
}

INITIAL {
	g = 0
	ninput = 0
}

BREAKPOINT {
	SOLVE state METHOD cnexp
	i = g*(v - e)
}

DERIVATIVE state {
	g' = -g/tau
}

VERBATIM
typedef struct RecvInfo {
	IvocVect* tvec;
	IvocVect* srcvec;
	IvocVect* tarvec;
} RecvInfo;
ENDVERBATIM

NET_RECEIVE (w (microsiemens), srcgid) {
	INITIAL { } : prevent srcgid from being set to 0
		g = g + w
		:printf("%g %g %g\n", t, srcgid, gid)
VERBATIM
		RecvInfo* rip = (RecvInfo*)_p_vecs;
		if (rip) {
			vector_append(rip->tvec, t);
			vector_append(rip->srcvec, _args[1]); /* srcgid */
			vector_append(rip->tarvec, gid);
		}
ENDVERBATIM
		ninput = ninput + 1
}

PROCEDURE set_record() {
VERBATIM
	RecvInfo** rip = (RecvInfo**)(&(_p_vecs));
	if (!(*rip)) {
		*rip = (RecvInfo*)hoc_Emalloc(sizeof(RecvInfo)); hoc_malchk();
	}
	(*rip)->tvec = vector_arg(1);
	(*rip)->srcvec = vector_arg(2);
	(*rip)->tarvec = vector_arg(3);
ENDVERBATIM
}

DESTRUCTOR {
VERBATIM
	if (_p_vecs) { free(_p_vecs); }
ENDVERBATIM
}
