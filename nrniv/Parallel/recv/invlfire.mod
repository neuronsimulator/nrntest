: dm/dt = (minf - m)/tau
: input event adds w to m
: when m = 1, or event makes m >= 1 cell fires
: minf is calculated so that the natural interval between spikes is invl

: Modified so that the invl can vary randomly by picking from a hoc
: Random instance.

: Modified to use in testing. The second weight should be
: set to the srcgid. On receive, the t srcgid gid
: is stored in three Vectors analogous to NetCon.record

NEURON {
	ARTIFICIAL_CELL IntervalFire
	RANGE tau, m, invl
	: m plays the role of voltage
	POINTER r, vecs
	RANGE noutput, ninput : count number of spikes generated and coming in
	RANGE gid
}

PARAMETER {
	tau = 5 (ms)   <1e-9,1e9>
	invl = 10 (ms) <1e-9,1e9> : varies if r is non-nil
}

ASSIGNED {
	m
	minf
	t0(ms)
	r
	tau1
	minf1
	ninput noutput
	gid vecs
}

INITIAL {
	ninput = 0
	noutput = 0
	tau1 = 1/tau
	minf = 1/(1 - exp(-invl*tau1)) : so natural spike interval is invl
	minf1 = 1/(minf - 1)
	specify_invl() : will change invl and minf if r is non-nil
	m = 0
	t0 = t
	net_send(firetime(), 1)
}

FUNCTION M() {
	M = minf + (m - minf)*exp(-(t - t0)*tau1)
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

NET_RECEIVE (w, srcgid) {
	INITIAL { } : prevent srcgid from being set to 0
	m = M()
	t0 = t
	if (flag == 0) {
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
		m = m + w
		if (m > 1) {
			m = 0
			noutput = noutput + 1
			net_event(t)
		}
		net_move(t+firetime())
	}else{
		net_event(t)
		noutput = noutput + 1
		m = 0
		specify_invl()
		net_send(firetime(), 1)
	}
}

FUNCTION firetime()(ms) { : m < 1 and minf > 1
	firetime = tau*log((minf-m)*minf1)
:	printf("firetime=%g\n", firetime)
}

PROCEDURE specify_invl() {
VERBATIM {
	extern double nrn_random_pick(void*);
	if (!_p_r) {
		return 0.;
	}
	invl = nrn_random_pick((void*)_p_r);
}
ENDVERBATIM
	minf = 1/(1 - exp(-invl*tau1)) : so natural spike interval is invl
	minf1 = 1/(minf - 1)
}

PROCEDURE set_rand() {
VERBATIM {
	extern void* nrn_random_arg(int);
	void** ppr;
	ppr = (void**)(&(_p_r));
	*ppr = nrn_random_arg(1);
}
ENDVERBATIM
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
