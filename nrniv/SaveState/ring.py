from neuron import h, gui
h.tstop = 100

h.load_file('netparmpi.hoc')
ncell = 128
pnm = h.ParallelNetManager(ncell)
pc = pnm.pc

# try with multiple threads
pnm.pc.nthread(32)

pnm.round_robin()

for i in range(ncell):
    if pnm.gid_exists(i):
        pnm.register_cell(i, h.IntFire1())


for i in range(ncell):
    pnm.nc_append(i, (i+1)%ncell, -1, 1.1, 2)


# stimulate
if pnm.gid_exists(4):
    stim = h.NetStim(.5)
    ncstim = h.NetCon(stim, pnm.pc.gid2obj(4))
    ncstim.weight[0] = 1.1
    ncstim.delay = 1
    stim.number = 1
    stim.start = 1

pnm.set_maxstep(100) # will end up being 2

pnm.want_all_spikes()

ss = h.SaveState()

def savestate():
    s = 'svst.{pcid}'.format(pcid = int(pc.id()))
    f = h.File(s)
    ss = h.SaveState()
    ss.save()
    ss.fwrite(f)


def restorestate():
    s = 'svst.{pcid}'.format(pcid = int(pc.id()))
    f = h.File(s)
    ss = h.SaveState()
    ss.fread(f)
    ss.restore()

def pspike():
    if pnm.myid == 0:
        print('\n')
        for i in range(int(pnm.spikevec.size())):
            print(pnm.spikevec.x[i], int(pnm.idvec.x[i]))


def prun(runState):
    h.stdinit()
    if runState == 1:
        pnm.psolve(h.tstop / 2.)
        savestate()
    else:
        restorestate()
    h.frecord_init()
    pnm.psolve(h.tstop)
    pspike()


prun(1)
prun(2)

pnm.pc.runworker()
pnm.pc.done()

