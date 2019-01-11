NEURON {
  POINT_PROCESS SinStim
  RANGE amp, freq
  ELECTRODE_CURRENT i
}

UNITS {
  pi = (pi)(1)
}

PARAMETER {
  amp = 0 (nanoamp)
  freq = 0 (1/s)
}

ASSIGNED {
  i (nanoamp)
}

BREAKPOINT {
  i = amp*sin(2*pi*freq*t*(.001))
}
