import hoc
h = hoc.HocObject()
h("proc p() { print ($o1) }")
h.p({})
h("allobjects()")

