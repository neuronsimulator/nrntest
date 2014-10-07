NEURON {
	POINT_PROCESS Test
}

FUNCTION_TABLE f(x)

FUNCTION g(x) {
  g = f(x)
}
