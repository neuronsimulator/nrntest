from neuron import h

pc = h.ParallelContext()


def func(i):
    print(("%d %g %g" % (i, h.hoc_ac_, pc.id())))
    return i


pc.runworker()

submit_id = [pc.submit(func, i) for i in range(3)]
print(("submit_id", submit_id))
while True:
    working_id = pc.working()
    if working_id == 0:
        break
    user_id = pc.userid()
    ret = pc.pyret()
    print(("working_id = %d user_id=%d ret=%d" % (working_id, user_id, ret)))
pc.done()
h.quit()
