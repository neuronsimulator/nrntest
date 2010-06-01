: can several thresholds be watched in a POINT_PROCESS?

NEURON {
	POINT_PROCESS YZW
	RANGE y, z, w
}

ASSIGNED { v y z w }

INITIAL {
	p()
}

AFTER SOLVE {
	p()
}

PROCEDURE p() {
	y = v
	z = v
	w = v
}

