from neuron import h
h.load_file("stdgui.hoc")

test = h.Test()

def foo(x=1, y=2):
	print "foo t=", h.t, " x=",x, " y=",y

test.set_callback((foo, (4, 6)))

h.cvode_active(1)
h.run()
