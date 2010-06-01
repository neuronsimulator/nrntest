: $Id: tcifb.mod,v 1.2 2005/10/12 19:36:46 hines Exp $

COMMENT
AP occurs when v becomes greater than vthresh
ENDCOMMENT

NEURON {
  POINT_PROCESS IFB
  NONSPECIFIC_CURRENT i
  GLOBAL hinf,tauh,tauh1,tauh2,vh,erev,vth,vreset
  RANGE gmax
}

PARAMETER {
  tauh1 = 100 (ms)
  tauh2 = 20 (ms)
  vh = -60
  erev = 120
  vth = -35
  vreset = -50
  gmax = 0.07 (mS/cm2)
}

ASSIGNED {
  v		(mV)		: postsynaptic voltage
  g
  i
  hinf
  tauh
  heaviside
}

STATE { h }

DEFINE init 1 DEFINE mid 2 DEFINE down 3 DEFINE up 4

INITIAL { 
  h = 1   
  net_send(0, init)
}

BREAKPOINT {
  SOLVE states METHOD cnexp
  i = heaviside*(gmax * h * (v-erev))
}

DERIVATIVE states {
  h' = (hinf-h)/tauh
}

NET_RECEIVE (w) {
	if (flag == init) {
printf("init t=%g v=%g\n", t, v)
		hinf = 1
		tauh = tauh2
		heaviside = 0
		WATCH (v < vh) down, (v > vth) up
	}
	if (flag == mid) {
printf("mid t=%g vh=%g vth=%g v=%g\n", t, vh, vth, v)
		hinf = 0  tauh = tauh1
		heaviside = 1
		WATCH (v < vh) down
		WATCH (v > vth) up
	}
	if (flag == down) {
printf("down t=%g vh=%g v=%g\n", t, vh, v)
		hinf = 1  tauh = tauh2
		heaviside = 0
		WATCH (v > vh) mid
	}
	if (flag == up) {
printf("up t=%g vth=%g v=%g\n", t, vth, v)
		net_event(t)
:		v = vreset
		WATCH (v < vh) down
		WATCH (v > vth-1) up
:		v = vreset
	}
}
