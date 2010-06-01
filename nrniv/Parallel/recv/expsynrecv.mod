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
	void* tvec;
	void* srcvec;
	void* tarvec;
} RecvInfo;
extern void* vector_arg(int iarg);
extern void vector_resize(void* vec, int size);
extern int vector_capacity(void* vec);
extern double* vector_vec(void* vec);
#define INFOCAST(ip) RecvInfo** ip = (RecvInfo**)(&(_p_vecs))
#define APPEND(vector,val) \
	vec = (*rip)->vector; \
	n = vector_capacity(vec); \
	vector_resize(vec, n+1); \
	pd = vector_vec(vec); \
	pd[n] = val;

ENDVERBATIM

NET_RECEIVE (w (microsiemens), srcgid) {
	INITIAL { } : prevent srcgid from being set to 0
		g = g + w
		:printf("%g %g %g\n", t, srcgid, gid)
VERBATIM
{
		int n;
		double* pd;
		void* vec;
		INFOCAST(rip);
		if (*rip) {
			APPEND(tvec, t);
			APPEND(srcvec, _args[1]); /* srcgid */
			APPEND(tarvec, gid);
		}
}
ENDVERBATIM
		ninput = ninput + 1
}

PROCEDURE set_record() {
VERBATIM
	void *a, *b, *c;
	INFOCAST(rip);
	a = vector_arg(1);
	b = vector_arg(2);
	c = vector_arg(3);
	if (!(*rip)) {
		*rip = (RecvInfo*)hoc_Emalloc(sizeof(RecvInfo)); hoc_malchk();
	}
	(*rip)->tvec = a;
	(*rip)->srcvec = b;
	(*rip)->tarvec = c;
ENDVERBATIM
}

DESTRUCTOR {
VERBATIM
	INFOCAST(rip);
	if (*rip) { free((void*)(*rip)); }
ENDVERBATIM
}
