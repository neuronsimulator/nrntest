NEURON {
  SUFFIX foo
  RANGE x
}

PARAMETER { x }

FUNCTION foo(y) {
  foo = x + y
}


FUNCTION bar(a, b) {
VERBATIM
{
  extern Section* chk_access();
  extern double nrn_call_mech_func(Symbol*, int narg, Prop*, int type);
  extern Node* node_exact(Section*, double);
  extern Prop* nrn_mechanism(int type, Node*);
  extern Symbol* hoc_lookup(const char*);
  extern void hoc_pushx(double);
  Node* nd = node_exact(chk_access(), _la);
  Symbol* sym = hoc_lookup("foo_foo");
  Prop* p = nrn_mechanism(_mechtype, nd);
  assert(sym);
  assert(p);
  assert(nd);
  hoc_pushx(_lb);
  _lbar = nrn_call_mech_func(sym, 1, p, _mechtype);
}
ENDVERBATIM
}
